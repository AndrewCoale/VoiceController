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
   "sprint": Key.shift,
    "menu": Key.esc,
    "inventory": "e",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "yes": Key.enter
}

mouse_command_map = {
   "left click": "left_click",
   "right click": "right_click"
}

camera_map = {
   "look up": (0, -500),
   "look down": (0, 500),
   "look left": (-500, 0),
   "look right": (500, 0),
   "look around": "360_view"
}

position_map = {
    "play": (500, 750),
    "new": (580, 120),
    "stake": (1050, 500),
    "steak": (1050, 500),
    "deck": (1050, 250),
    "first": (750, 750),
    "second": (1000, 330),
    "third": (1200, 370)
}


def send_key(command, duration=0.1):
    key = command_map.get(command)
    if key:
        keyboard.press(key)
        time.sleep(duration)  # Hold the key for a short duration
        keyboard.release(key)
    else:
       keyboard.press('a')
       keyboard.release('a')

def perform_mouse_action(action):
    if action == "left_click":
        mouse.press(Button.left)
        time.sleep(10.0)
        mouse.release(Button.left)
    elif action == "right_click":
        mouse.press(Button.right)
        time.sleep(0.1)
        mouse.release(Button.right)
    else:
        print(f"Mouse action '{action}' not recognized")

def move_camera(movement):
    if movement == "360_view":
        for _ in range(36):
            pydirectinput.move(10, 0)
            time.sleep(0.05)
    else:
        dx, dy = movement
        pydirectinput.moveRel(dx, dy, relative=True)

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


focus_window("Minecraft") # change name to specify focus window
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
        elif command in command_map:
            send_key(command, 3.0)
        elif command in mouse_command_map:
            perform_mouse_action(mouse_command_map[command])
        elif command in camera_map:
            move_camera(camera_map[command])
except KeyboardInterrupt:
    print("Stopping...")
