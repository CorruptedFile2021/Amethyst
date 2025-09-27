import os
import json
import webview
import util_func
import pyautogui
import backend_functions
import threading
import pyautogui
from argostranslate import package as argos_package
import webview.platforms
import argostranslate.translate
import pathlib
import pystray
from PIL import Image
import sys


Windows = []


def create_image():
  image = Image.open("images\logo_1.png")
  return image

def on_quit(icon, item):
  icon.stop()
  for window in Windows:
      window.destroy()
  sys.exit()

def on_window_close():
  MainWindow.hide()
  TranslationWindow.hide()
  return False



DEFAULT_SETTINGS_JSON = """{
  "Name": "USER_NAME",
  "Api_Keys": {
    "OPEN_AI": "",
    "GOOGLE_TRANSLATE": ""
  },
  "Short_Cut_Keys": {
    "Translate": "ctrl+shift+y"
  }
}
"""

CURRENT_DIRECTORY = os.getcwd()
screen_width, screen_height = pyautogui.size()


Appwidth, Appheight = util_func.scaled_for_screen(1200,750,2560,1440,screen_width,screen_height)

print(f" CURRENT DIRECTORY: {CURRENT_DIRECTORY}")

if os.path.isfile(f"{CURRENT_DIRECTORY}/settings.json"):
    print("NOT FIRST STARTUP: READING SETTINGS")
    with open("settings.json","r") as settings_json_file:
        settings_content = json.load(settings_json_file)

        USER_NAME = settings_content["Name"]
        OPEN_AI_KEY = settings_content["Api_Keys"]["OPEN_AI"]
        GOOGLE_TRANSLATE_KEY = settings_content["Api_Keys"]["GOOGLE_TRANSLATE"]
        TRANSLATE_SHORTCUT_KEY = settings_content["Short_Cut_Keys"]["Translate"]



else:
    print("FIRST STARTUP DETECTING: STARTING SETUP")
    print("CREATING SETTINGS.JSON FILE")
    with open("settings.json","w") as settings_json_file:
        settings_json_file.write(DEFAULT_SETTINGS_JSON)
    
    models_folder = pathlib.Path("translate_models")

    # Install all packages in the folder
    for model_file in models_folder.glob("*.argosmodel"):
      print(f"Installing {model_file.name}...")
      argos_package.install_from_path(model_file)


    argostranslate.translate.load_installed_languages()
    
        

MainWindow = webview.create_window(
    "Amethyst",
    "frontend/main.html", 
    width=Appwidth,
    height=Appheight,
    resizable=False,
    js_api=backend_functions.BACKEND_FUNCTIONS(),    
)

TranslationWindow = webview.create_window(
    "Tanslation Output",
    "frontend/translation_result.html",
    width=800,
    height=200,
    resizable=False,
    frameless=True,
    transparent=True,
)

#TranslationWindow.events.loaded += apply_blur


Windows.append(MainWindow)
Windows.append(TranslationWindow)



MainWindow.events.closing += on_window_close

def setup_tray():
    icon = pystray.Icon("Amethyst", create_image(), "Amethyst")
    icon.menu = pystray.Menu(
      pystray.MenuItem("Show App", lambda: MainWindow.show()),
      pystray.MenuItem("Quit", on_quit),
    )
    icon.run()

threading.Thread(target=setup_tray, daemon=True).start()
threading.Thread(target=backend_functions.translate_hotkey_listener, daemon=True).start()

webview.start(gui='edgechromium', func=None, debug=False, http_server=True)



