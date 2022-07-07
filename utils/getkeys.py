import win32api as wapi
import ctypes

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if 'H' in keys:
        return 'H'
    elif 'B' in keys:
        return 'B'
    elif 'A' in keys:
        return 'A'
    elif 'D' in keys:
        return 'D'
    elif ' ' in keys:
        return ' '
    else:
        return 'W'


def mouse_check():
    if ctypes.windll.user32.GetKeyState(0x01) == 0x0002:
        return 'L'
