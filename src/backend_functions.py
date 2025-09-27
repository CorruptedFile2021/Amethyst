import requests
import json
import os
import keyboard
import pyautogui
import time
import pyperclip
from libretranslate.main import main as lt_main
import threading
import webview


Translation_Windows_List = []


with open("settings.json","r") as settings_json_file:
        settings_content = json.load(settings_json_file)
        TRANSLATE_SHORTCUT_KEY = settings_content["Short_Cut_Keys"]["Translate"]
        print(TRANSLATE_SHORTCUT_KEY)
        settings_json_file.close()

class BACKEND_FUNCTIONS:
    def __init__(self):
        translation_server_thread = threading.Thread(target=self.run_translation_service, daemon=True)
        translation_server_thread.start()
        with open("settings.json","r") as settings_json_file:
            settings_content = json.load(settings_json_file)
            self.USER_NAME = settings_content["Name"]
            self.OPEN_AI_KEY = settings_content["Api_Keys"]["OPEN_AI"]
            self.GOOGLE_TRANSLATE_KEY = settings_content["Api_Keys"]["GOOGLE_TRANSLATE"]
            self.TRANSLATE_SHORTCUT_KEY = settings_content["Short_Cut_Keys"]["Translate"]
            

    def run_translation_service(self):
        lt_main()
        





def grab_text_selection():
    try:
        old_content = pyperclip.paste()
        pyautogui.hotkey("ctrl","c")
        time.sleep(0.05)
        new_content = pyperclip.paste()
        if new_content == old_content:
            print("NO NEW CONTENT WAS SELECTED, NOT CONTINUING")
        else:
            return new_content, old_content
    except:
        pass

def on_translate_hotkey():
    try:
        text_to_translate, old_content = grab_text_selection()
        #pyperclip.copy(old_content)
        if text_to_translate.strip():        
            print("Captured:", text_to_translate)

            TRANSLATE_REQUEST_INFO = {
                "q" : text_to_translate,
                "source": "auto",
                "target": "en",
                "format": "text",
                "alternatives": 3
            }
            translation_response = requests.post(url="http://127.0.0.1:5000/translate",data=TRANSLATE_REQUEST_INFO)
            print(translation_response.json())
    except:
        pass



def translate_hotkey_listener():
    keyboard.add_hotkey(TRANSLATE_SHORTCUT_KEY, on_translate_hotkey)
    keyboard.wait()