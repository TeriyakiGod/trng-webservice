import struct
import collections
from channels.generic.websocket import WebsocketConsumer

class TrngConsumer(WebsocketConsumer):
    buffer: collections.deque[int] = collections.deque(maxlen=1000)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, bytes_data: bytes):
        if bytes_data:
            # Convert bytes to unsigned int
            random_number = int.from_bytes(bytes_data, byteorder='little', signed=False)
            # Add the random number to the buffer
            TrngConsumer.buffer.appendleft(random_number)
        else:
            print("Received empty data.")