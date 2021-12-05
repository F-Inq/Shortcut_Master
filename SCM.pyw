from keyboard import read_key, press_and_release, wait
from os import system, startfile, path
from time import sleep
from ctypes import windll

from shortcuts import action_list, link_list
from abbreviations import add_all_abbreviations


def check_if_abbreviation(some_key):
    if some_key == 'shift':  # user wants an abbreviation
        wait('space')  # space is an abbreviation call
        sleep(0.2)  # without delay quits before filling the abbreviation
        quit()


add_all_abbreviations()  # keyboard.add_abbreviation() for all emails from abbreviations.py

key_1 = read_key(suppress=True)
sleep(0.15)  # keys can be read twice if held down
check_if_abbreviation(key_1)
key_2 = read_key(suppress=True)
check_if_abbreviation(key_2)
sleep(0.15)  # suppress=True fails on key release if there's no sleep()
shortcut = key_1 + key_2

if shortcut in action_list:
    if action_list[shortcut] == 'Lock':
        sleep(0.5)
        windll.user32.LockWorkStation()  # lock pc
        quit()
    elif action_list[shortcut] == 'Screenshot':
        press_and_release('win+shift+s')  # make a screenshot
    elif action_list[shortcut] == 'Sleep':
        sleep(0.5)
        system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')  # put pc to sleep
        quit()

if shortcut in link_list:
    link_exe = path.dirname(__file__) + '\\links\\' + link_list[shortcut]
    try:
        startfile(link_exe)
    except FileNotFoundError:
        quit()

quit()
