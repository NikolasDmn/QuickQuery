from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyautogui
import pyperclip
import webbrowser
import time
import tkinter as tk
from tkinter import simpledialog

# Set to keep track of currently pressed keys
current_keys = set()

# Read configurations from a .conf file
def read_config(file_path):
    try:
        # Open and parse the configuration file
        with open(file_path, 'r') as file:
            return {key.strip(): value.strip() for key, value in 
                    (line.split(' = ') for line in file if line.strip())}
    except FileNotFoundError:
        print(f"Error: Configuration file {file_path} not found.")
        return {"URL": ""}

# Simulate paste operation and press enter
def paste_text():
    pyautogui.hotkey('ctrl', 'v')  # Paste
    time.sleep(0.1)
    pyautogui.press('enter')  # Press Enter

# Open a new browser tab with the given URL and paste the prompt
def ask_gpt(prompt):
    URL = read_config("C:\\Users\\diama\\OneDrive\\Coding\\GPTSearcher\\config.conf")['URL']
    webbrowser.open_new_tab(URL)
    if prompt or prompt.strip() != "":
        pyperclip.copy(prompt)
        time.sleep(2)
        paste_text()

# Copy currently highlighted text to clipboard
# Delays are to ensure clipboard is updated
def copy_highlighted_text_to_clipboard():
    keyboard = Controller()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1) 

# Get highlighted text, return None if no new text is highlighted
def get_highlighted():
    prev_clipboard = pyperclip.paste()
    start_time = time.time()
    while time.time() - start_time < 2:
        copy_highlighted_text_to_clipboard()
        current_text = pyperclip.paste()
        if current_text != prev_clipboard:
            return current_text
    return None


# Primary function to fetch and process highlighted text
def search():
    ask_gpt(get_highlighted())
    
# Event handler for keyboard events
def on_key_event(key, is_press):
    try:
        if is_press:
            current_keys.add(key)
            if {Key.ctrl_l, Key.alt_l, Key.space} <= current_keys:
                current_keys.clear()
                search()
        else:
            current_keys.discard(key)
    except AttributeError:
        pass


# Setup and start the keyboard listener
def setup_listener():
    listener = keyboard.Listener(
        on_press=lambda key: on_key_event(key, True),
        on_release=lambda key: on_key_event(key, False))
    listener.start()
    listener.join()


def main():
    setup_listener()

if __name__ == "__main__":
    main()
