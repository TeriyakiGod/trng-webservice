import random
from django.conf import settings
from .consumers import TrngConsumer
import asyncio

## @brief This function returns a random number from a circular buffer that is filled by the websocket consumer.
#  @return A random integer in range from 0 to 4294967295.
async def rng() -> int:
    if settings.DEBUG:
        return random.randint(0, 4294967295)
    i=0
    # Wait for the buffer to fill if it's empty
    while not TrngConsumer.buffer:
        # If the buffer is empty for 10 seconds, raise an error. It's likely that the TRNG device is not working or the websocket connection is down.
        i+=1
        if i>100:
            raise asyncio.TimeoutError("Timeout occurred while waiting for numbers in the buffer. Check the TRNG device and the websocket connection.")
        await asyncio.sleep(0.1)
    return int(TrngConsumer.buffer.pop())
