import os
import json
import time
import webview
import util_func
import pyautogui
import requests
import backend_functions
import keyboard
import threading
import pyautogui
import pyperclip

DEFAULT_SETTINGS_JSON = """{
  "Name": "USER_NAME",
  "Api_Keys": {
    "OPEN_AI": "",
    "GOOGLE_TRANSLATE": ""
  },
  "Short_Cut_Keys": {
    "Translate": "ctrl+shift+t"
  }
}
"""

CURRENT_DIRECTORY = os.getcwd()
screen_width, screen_height = pyautogui.size()


Appwidth, Appheight = util_func.scaled_for_screen(1200,750,2560,1440,screen_width,screen_height)
print(Appwidth,Appheight)

print(f" CURRENT DIRECTORY: {CURRENT_DIRECTORY}")

if os.path.isfile(f"{CURRENT_DIRECTORY}/settings.json"):
    print("NOT FIRST STARTUP: READING SETTINGS")
    with open("settings.json","r") as settings_json_file:
        settings_content = json.load(settings_json_file)
        print(settings_content["Name"])
        print(settings_content["Api_Keys"]["OPEN_AI"])

        USER_NAME = settings_content["Name"]
        OPEN_AI_KEY = settings_content["Api_Keys"]["OPEN_AI"]
        GOOGLE_TRANSLATE_KEY = settings_content["Api_Keys"]["GOOGLE_TRANSLATE"]
        TRANSLATE_SHORTCUT_KEY = settings_content["Short_Cut_Keys"]["Translate"]



else:
    print("FIRST STARTUP DETECTING: STARTING SETUP")
    print("CREATING SETTINGS.JSON FILE")
    with open("settings.json","w") as settings_json_file:
        settings_json_file.write(DEFAULT_SETTINGS_JSON)
        

window = webview.create_window(
    "Amethyst",
    "frontend/main.html", 
    width=Appwidth,
    height=Appheight,
    resizable=False,
    js_api=backend_functions.BACKEND_FUNCTIONS()
)

threading.Thread(target=backend_functions.translate_hotkey_listener, daemon=True).start()

webview.start(gui='edgechromium', func=None, debug=False, http_server=True)


