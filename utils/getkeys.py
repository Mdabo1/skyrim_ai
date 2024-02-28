# # Citation: Box Of Hats (https://github.com/Box-Of-Hats )

# import win32api as wapi
# import time

# keyList = ["\b"]
# for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
#     keyList.append(char)


from win32api import GetKeyState
import win32api
import time
import pydirectinput

special_keys = [0x01, 0x02, 0x10, 0x20, 0x12]

special = {
    0x01: "leftClick",
    0x02: "rightClick",
    0x10: "shift",
    0x20: "space",
    0x12: "alt",
}


def key_check():
    keys = []
    for i in range(1, 256):
        if win32api.GetAsyncKeyState(i):
            if i in special_keys:
                keys.append(special[i])
            else:
                keys.append(chr(i))
    time.sleep(0.01)
    return keys


def mouse_check():
    x, y = pydirectinput.position()
    position1 = [x, y]
    time.sleep(0.01)
    x, y = pydirectinput.position()
    position2 = [x, y]
    return [position2[0] - position1[0], position2[1] - position1[1]]
