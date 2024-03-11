import time, os, struct
from channels.generic.websocket import WebsocketConsumer

class TrngConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = time.time()
        self.total_bytes = 0

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, bytes_data: bytes):
        if bytes_data:
            # Convert bytes to unsigned int
            random = struct.unpack('<I', bytes_data)[0]

            # Update total bytes received
            self.total_bytes += len(bytes_data)

            # save the random number to a file
            with open('random_numbers.txt', 'a') as file:
                file.write(f"{random}\n")

            # Check if a second has passed since the last print
            if time.time() - self.start_time >= 1:
                # Calculate average speed in KBs per second
                avg_speed_kb = self.total_bytes / 1024
                print(f"Average download speed: {avg_speed_kb:.2f} Kb per second", end=" | ")
                print(f"Total data received: {(os.path.getsize('random_numbers.txt') / 1024)} Kb", end="\r")
                self.start_time = time.time()
                self.total_bytes = 0
        else:
            print("Received empty data.")