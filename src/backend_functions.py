import requests
import json
import os
import keyboard
import pyautogui
import time
import pyperclip
class BACKEND_FUNCTIONS:
    def __init__(self):
        with open("settings.json","r") as settings_json_file:
            settings_content = json.load(settings_json_file)
            self.USER_NAME = settings_content["Name"]
            self.OPEN_AI_KEY = settings_content["Api_Keys"]["OPEN_AI"]
            self.GOOGLE_TRANSLATE_KEY = settings_content["Api_Keys"]["GOOGLE_TRANSLATE"]
            self.TRANSLATE_SHORTCUT_KEY = settings_content["Short_Cut_Keys"]["Translate"]
            
    
    def Button_Click(self,string):
        print("Button Clicked!")
        


def grab_text_selection():
    old_content = pyperclip.paste()
    pyautogui.hotkey("ctrl","c")
    time.sleep(0.05)
    return pyperclip.paste(), old_content

def on_hotkey():
    text_to_translate, old_content = grab_text_selection()
    pyperclip.copy(old_content)
    if text_to_translate.strip():        
        print("Captured:", text_to_translate)

def translate_hotkey_listener():
    keyboard.add_hotkey('ctrl+shift+t', on_hotkey)  # custom shortcut
    keyboard.wait()