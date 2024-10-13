import collections
from ctypes import c_uint32
import struct
from channels.generic.websocket import WebsocketConsumer
import requests
from . import logger

class TrngConsumer(WebsocketConsumer):
    # Circular buffer to store random numbers
    # The size of the buffer is 100 MB
    buffer_size = 100000000
    buffer: collections.deque[c_uint32] = collections.deque(maxlen=buffer_size)
    generators = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        self.generators += 1
        self.accept()

    def disconnect(self, close_code):
        self.generators -= 1

    def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            # Convert bytes to unsigned int
            random_number: c_uint32 = struct.unpack('<I', bytes_data)[0]
            # Add the random number to the buffer
            self.buffer.appendleft(random_number)
        elif text_data:
            logger.info(f"Received text data: {text_data}")
            pass
        else:
            logger.info("Received unidentified data")
            pass