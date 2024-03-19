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

def get_int(n: int, min: int, max: int) -> list[int]:
    return [random_to_int((max+1) - min) + min for _ in range(n)]

def get_float(n: int, precision: int) -> list[float]:
    return [random_to_float(precision) for _ in range(n)]