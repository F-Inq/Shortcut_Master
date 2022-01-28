from keyboard import read_key, press_and_release, wait
from os import system, startfile, path
from time import sleep
from ctypes import windll

from shortcuts import action_list, link_list
from abbreviations import add_all_abbreviations


def check_special_case(some_key):
    if some_key == 'shift':  # user wants an abbreviation
        wait('space')  # space is an abbreviation call
        sleep(0.2)  # without delay quits before filling the abbreviation
        quit()
    elif some_key == 'space':  # user wants to quit
        quit()


add_all_abbreviations()  # keyboard.add_abbreviation() for all emails from abbreviations.py

key_1 = read_key(suppress=True)
check_special_case(key_1)

while True:
    key_2 = read_key(suppress=True)
    check_special_case(key_2)
    shortcut = (key_1 + key_2).lower()
    if shortcut in action_list:
        command = action_list[shortcut]
        if command == 'Lock':
            sleep(0.5)
            windll.user32.LockWorkStation()  # lock pc
            quit()
        elif command == 'Screenshot':
            press_and_release('win+shift+s')  # make a screenshot
            key_3 = read_key()  # wait until user makes the screenshot before killing the usually bugged screenshot exe
            if key_3:
                if key_3 == 'ctrl':
                    sleep(1.5)
                system('taskkill /IM "ScreenClippingHost.exe" /F')  # kill screenshot exe if it bugged for some reason
                quit()
        elif command == 'Sleep':
            sleep(0.5)
            system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')  # put pc to sleep
            quit()
    if shortcut in link_list:
        name_exe = link_list[shortcut]
        link_exe = path.dirname(__file__) + '\\links\\' + name_exe
        try:
            startfile(link_exe)
        except FileNotFoundError:
            pass
        quit()
