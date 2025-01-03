from django.core.cache import cache
import struct
from ctypes import c_uint32
from channels.generic.websocket import WebsocketConsumer
import collections
from . import logger

class TrngConsumer(WebsocketConsumer):
    buffer_size = 100000000
    buffer: collections.deque[c_uint32] = collections.deque(maxlen=buffer_size)
    
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            random_number: c_uint32 = struct.unpack('<I', bytes_data)[0]
            self.buffer.appendleft(random_number)
        elif text_data:
            logger.info(f"Received text data: {text_data}")
        else:
            logger.info("Received unidentified data")

    @classmethod
    def get_buffer_size(cls):
        """Returns the current number of random numbers in the buffer."""
        return len(cls.buffer)