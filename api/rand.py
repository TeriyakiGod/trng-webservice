from trng.interface import rng
from PIL import Image
from . import UINT32_MAX
import numpy as np

## @brief This function scales uint32 random numbers 
# to an integer within a given range using 
# Lemire's Method: Debiased Integer Multiplication. 
#  @param range The range within which to generate the random integer.
#  @return A random integer within the given range.
async def random_to_int(range: int) -> int:
    x = await rng()
    m = x * range
    l = m & 0xFFFFFFFF  # Lower 32 bits of the product
    t = (1 << 32) % range  # Calculate rejection threshold
    
    # Reject biased values
    if l < t:
        while l < t:
            x = await rng()
            m = x * range
            l = m & 0xFFFFFFFF
    
    # Return the high 32 bits
    return m >> 32


## @brief This function scales a uint32 random number to
#  a random float with a given precision.
#  @param precision The precision of the generated float.
#  @return A random float with the given precision.
async def random_to_float(precision: int) -> float:
    return round(await rng() / UINT32_MAX, precision)

## @brief This function scales uint32 random numbers to a random byte array of a given length.
#  @param n The length of the byte array to generate.
#  @return A random byte array of the given length.
async def random_to_bytes(n: int) -> bytes:
    byte_array = bytearray()
    
    # Generate full 4-byte chunks
    for _ in range(n // 4):
        x = await rng()  # Get a random uint32 number
        byte_array.extend(x.to_bytes(4, 'little'))  # Convert uint32 to bytes and add to the array
    
    # Handle any remaining bytes (if n is not a multiple of 4)
    remainder = n % 4
    if remainder > 0:
        x = await rng()  # Get another random uint32 number
        byte_array.extend(x.to_bytes(4, 'little')[:remainder])  # Add only the necessary remainder bytes
    
    return bytes(byte_array)  # Convert the bytearray to immutable bytes and return


## @brief This function generates a list of random integers within a given range.
#  @param n The number of integers to generate.
#  @param min The minimum value of the range.
#  @param max The maximum value of the range.
#  @param repeat Whether to allow repeated values in the list. If True the n has to be less than the length of the range.
#  @return A list of random integers within the given range.
async def get_int(n: int, min: int, max: int, repeat: bool = True) -> list[int]:
    if repeat:
        return [await random_to_int((max+1) - min) + min for _ in range(n)]
    else:
        if n > (max - min + 1):
            raise ValueError('The number of integers to generate must be less than the length of the range.')
        seq = [i for i in range(min, max+1)]
        return [seq.pop(await random_to_int(len(seq))) for _ in range(n)]
        
## @brief This function generates a list of random floats with a given precision.
#  @param n The number of floats to generate.
#  @param precision The precision of the generated floats.
#  @return A list of random floats with the given precision.
async def get_float(n: int, precision: int) -> list[float]:
    return [await random_to_float(precision) for _ in range(n)]

## @brief This function generates a list of strings representing bytes in a given format.
#  @param n The number of bytes to generate.
#  @param f The format in which to represent the bytes. Can be one of ['h', 'o', 'b', 'd'] or it defaults to hexadecimal.
#  @return A list of strings representing bytes in the given format.
async def get_bytes(n: int, f: str) -> list[str]:
    match f:
        # Hexadecimal
        case 'h':
            return [format(b, '02x') for b in bytearray(await random_to_bytes(n))]
        # Octal
        case 'o':
            return [format(b, '03o') for b in bytearray(await random_to_bytes(n))]
        # Binary
        case 'b':
            return [format(b, '08b') for b in bytearray(await random_to_bytes(n))]
        # Decimal
        case 'd':
            return [format(b, '03d') for b in bytearray(await random_to_bytes(n))]
        # Default to hexadecimal    
        case default:
            return [format(b, '02x') for b in bytearray(await random_to_bytes(n))]
            
## @brief This function generates a random string of a given length.
#  @param n The length of the string to generate.
#  @param digits Whether to include digits in the string.
#  @param letters Whether to include letters in the string.
#  @param special Whether to include special characters in the string.
#  @return A random string of the given length.            
async def get_strings(n: int, m: int, digits: bool, letters: bool, special, repeat: bool) -> list[str]:
    # Define the character sets
    # All characters: 33 - 126
    # Digits: 48 - 57
    # Letters: 65 - 90, 97 - 122
    # Special characters: 33 - 47, 58 - 64, 91 - 96, 123 - 126
    digit_list = [chr(i) for i in range(48, 58)]
    letter_list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    special_list = [chr(i) for i in range(33,47)] + [chr(i) for i in range(58,65)] + [chr(i) for i in range(91,97)] + [chr(i) for i in range(123,127)]
    char_list = []
    if digits:
        char_list += digit_list
    if letters:
        char_list += letter_list
    if special:
        char_list += special_list
    word_list:list[str] = []
    for i in range(n):
        if repeat:
            word = ''.join([char_list[await random_to_int(len(char_list))] for _ in range(m)])
        else:
            if m > len(char_list):
                raise ValueError("m cannot be greater than the number of available characters")
            word = ''.join([char_list.pop(await random_to_int(len(char_list))) for _ in range(m)]) #TODO: IndexError: pop from empty list - FIX IT
        word_list.append(word)
    return word_list
        
## @brief This function generates a list of integers between min and max in random order.
#  @param min The minimum value of the range.
#  @param max The maximum value of the range.
#  @return A list of integers from min to max in random order.
async def get_sequence(min: int, max: int) -> list[int]:
    sequence = [i for i in range(min, max + 1)]
    for i in range(len(sequence) - 1, 0, -1):  # Fisher-Yates shuffle
        j = await random_to_int(i + 1)  # Get a random index in [0, i]
        sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence
        
## @brief This function generates a list of n random coin flips (represented as strings).
#  @param n The number of coin flips to generate.
#  @return A list of strings representing coin flips.
async def get_coin_flips(n: int) -> list[str]:
    return ['Obverse' if await random_to_int(2) == 0 else 'Reverse' for _ in range(n)]

## @brief This function generates a list of n random dice rolls with m sides.
#  @param n The number of dice rolls to generate.
#  @param m The number of sides on the dice.
#  @return A list of n random dice rolls with m sides.
async def get_dice_rolls(n: int, m: int) -> list[int]:
    return [await random_to_int(m) + 1 for _ in range(n)]

## @brief This function generates a list of n random lotto numbers.
#  @param n The number of lotto numbers to generate.
#  @return A list of n random lotto numbers.
async def get_lotto(n: int) -> list[list[int]]:
        return [await get_int(6, 1, 49, False) for _ in range(n)]
    

async def get_bitmap(width: int, height: int, zoom_factor: int) -> Image.Image:
    # Calculate the total number of pixels
    total_pixels = width * height

    # Generate random bytes
    random_bytes = await random_to_bytes(total_pixels // 8 + (total_pixels % 8 > 0))

    # Convert the bytes to a bit array
    bit_array = np.unpackbits(np.frombuffer(random_bytes, dtype=np.uint8))

    # Reshape the bit array to match the image dimensions
    bit_array = bit_array[:width*height].reshape((height, width))

    # Repeat the rows and columns based on the zoom factor
    bit_array = np.repeat(np.repeat(bit_array, zoom_factor, axis=0), zoom_factor, axis=1)

    # Create a new image from the bit array
    img = Image.fromarray(np.uint8(bit_array)*255, 'L')

    return img

async def get_grayscale_bitmap(width: int, height: int, zoom_factor: int) -> Image.Image:
    # Calculate the total number of pixels
    total_pixels = width * height

    # Generate random bytes
    byte_array = np.array([int.from_bytes(await random_to_bytes(1), 'big') for _ in range(total_pixels)], dtype=np.uint8)

    # Reshape the byte array to match the image dimensions
    byte_array = byte_array.reshape((height, width))

    # Repeat the rows and columns based on the zoom factor
    byte_array = np.repeat(np.repeat(byte_array, zoom_factor, axis=0), zoom_factor, axis=1)

    # Create a new image from the byte array
    img = Image.fromarray(byte_array, mode='L')

    return img

## @brief This function generates a random RGB noise image with a given zoom factor.
#  @param width The width of the image.
#  @param height The height of the image.
#  @param zoom_factor The factor by which to zoom the image.
#  @return A PIL Image object representing the RGB noise image.
async def get_rgb_noise_image(width: int, height: int, zoom_factor: int) -> Image.Image:
    # Calculate the total number of pixels
    total_pixels = width * height

    # Generate random bytes for each color channel in one go
    red_bytes = await random_to_bytes(total_pixels)
    green_bytes = await random_to_bytes(total_pixels)
    blue_bytes = await random_to_bytes(total_pixels)

    # Convert the random bytes to numpy arrays for each channel
    red_channel = np.frombuffer(red_bytes, dtype=np.uint8).reshape((height, width))
    green_channel = np.frombuffer(green_bytes, dtype=np.uint8).reshape((height, width))
    blue_channel = np.frombuffer(blue_bytes, dtype=np.uint8).reshape((height, width))

    # Apply zoom factor by repeating rows and columns for each channel
    red_channel = np.repeat(np.repeat(red_channel, zoom_factor, axis=0), zoom_factor, axis=1)
    green_channel = np.repeat(np.repeat(green_channel, zoom_factor, axis=0), zoom_factor, axis=1)
    blue_channel = np.repeat(np.repeat(blue_channel, zoom_factor, axis=0), zoom_factor, axis=1)

    # Stack the color channels to create an RGB image
    rgb_image = np.dstack((red_channel, green_channel, blue_channel))

    # Create a new RGB image from the array
    img = Image.fromarray(rgb_image, 'RGB')

    return img

async def get_colors(n: int) -> list[str]:
    return ["#"+("".join(await get_bytes(3, "h"))) for _ in range(n)]