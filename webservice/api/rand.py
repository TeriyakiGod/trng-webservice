## @package rand
# This module provides functions to generate random numbers and byte arrays.
# It uses the trng interface to get random numbers from the hardware random number generator.
# It also provides functions to convert the random numbers to integers, floats, and byte arrays.

from trng.interface import rng
from typing import Final

## The maximum value of a uint32.
# @var UINT32_MAX
UINT32_MAX: Final[int] = 4294967295

## @brief This function scales uint32 random numbers to an integer within a given range using Lemire's Method: Debiased Integer Multiplication. 
#  @param range The range within which to generate the random integer.
#  @return A random integer within the given range.
async def random_to_int(range: int) -> int:
    x = await rng()
    m = x * range
    l = m & 0xFFFFFFFF
    if (l < range):
        t = -range % range
        while (l < t):
            x = await rng()
            m = x * range
            l = m & 0xFFFFFFFF
    return m >> 32

## @brief This function scales a uint32 random number to a random float with a given precision.
#  @param precision The precision of the generated float.
#  @return A random float with the given precision.
async def random_to_float(precision: int) -> float:
    return round(await rng() / UINT32_MAX, precision)

## @brief This function scales uint32 random numbers to a random byte array of a given length.
#  @param n The length of the byte array to generate.
#  @return A random byte array of the given length.
async def random_to_bytes(n: int) -> bytes:
    byte_array = bytearray()
    for _ in range(n):
        byte_array.append(await random_to_int(256))
    return bytes(byte_array)

## @brief This function generates a list of random integers within a given range.
#  @param n The number of integers to generate.
#  @param min The minimum value of the range.
#  @param max The maximum value of the range.
#  @return A list of random integers within the given range.
async def get_int(n: int, min: int, max: int) -> list[int]:
    return [await random_to_int((max+1) - min) + min for _ in range(n)]

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
            