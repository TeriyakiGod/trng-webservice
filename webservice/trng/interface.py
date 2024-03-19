from .consumers import TrngConsumer
import time

def rng() -> int:
    # Wait for the buffer to fill if it's empty
    while not TrngConsumer.buffer:
        time.sleep(0.01)  # wait for 10ms
    return int(TrngConsumer.buffer.pop())