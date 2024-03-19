from enum import Enum
from locale import format_string
from matplotlib.pylab import f
from traitlets import default
from trng.interface import rng
from typing import Final

UINT32_MAX: Final[int] = 4294967295

def random_to_int(range: int) -> int:
    # Debiased Integer Multiplication — Lemire's Method
    x = rng()
    m = x * range
    l = m & 0xFFFFFFFF
    if (l < range):
        t = -range % range
        while (l < t):
            x = rng()
            m = x * range
            l = m & 0xFFFFFFFF
    return m >> 32

def random_to_float(precision: int) -> float:
    return round(rng() / UINT32_MAX, precision)

def random_to_bytes(n: int) -> bytes:
    byte_array = bytearray()
    for _ in range(n // 4):
        byte_array.extend(rng().to_bytes(4, 'big'))
    if n % 4 != 0:
        byte_array.extend(rng().to_bytes(n % 4, 'big'))
    return bytes(byte_array)

def get_int(n: int, min: int, max: int) -> list[int]:
    return [random_to_int((max+1) - min) + min for _ in range(n)]

def get_float(n: int, precision: int) -> list[float]:
    return [random_to_float(precision) for _ in range(n)]

def get_bytes(n: int, f: str) -> list[str]:
    match f:
        case 'h':
            return [b.to_bytes(1,"big").hex() for b in bytearray(random_to_bytes(n))]
        case default:
            return [b.to_bytes(1,"big").hex() for b in bytearray(random_to_bytes(n))]
            