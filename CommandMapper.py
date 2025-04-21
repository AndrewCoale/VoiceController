from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Button, Controller as MouseController
import pydirectinput
import time
from VoiceConverter import *
import pygetwindow as gw


keyboard = KeyController()
mouse = MouseController()


command_map = {
   "forward": "w",
   "back": "s",
   "left": "a",
   "right": "d",
   "jump": Key.space,
   "sprint": Key.shift
}

position_map = {
    "play": (500, 750),
    "new": (580, 120),
    "stake": (1050, 500),
    "steak": (1050, 500),
    "deck": (1050, 250),
    "start": (750, 650)
}


def send_key(command):
   key = command_map.get(command)
   if key:
       keyboard.press(key)
       keyboard.release(key)
   else:
       keyboard.press('a')
       keyboard.release('a')


def focus_window(title):
   #windows = gw.getWindowsWithTitle("Minecraft")
   windows = gw.getWindowsWithTitle(title)
   if windows:
       windows[0].activate()
       time.sleep(0.5)

def click(position):
    #pydirectinput.moveTo()
    pydirectinput.click(position[0], position[1])

def reset():
    key = "r"
    keyboard.press(key)
    time.sleep(5)
    keyboard.release(key)


focus_window("Balatro")
#for i in range(20):
   #send_key(get_voice_command())

def start_run():
    click(position_map["play"])
    click(position_map["new"])
    click(position_map["stake"])
    click(position_map["start"])
    click(position_map["start"])
    time.sleep(5)

try:
    while True:
        command = get_voice_command()
        if 'reset' in str(command):
            reset()
        elif command in position_map:
            click(position_map[command])
except KeyboardInterrupt:
    print("Stopping...")
