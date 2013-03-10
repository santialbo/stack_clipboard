#!/usr/bin/python
from pyperclip import setcb, getcb
import pickle
import sys, os, platform

CB_PATH = os.path.join(os.path.expanduser("~"), ".clipboard")
CB_SIZE = 100

def open_cb(perm):
    try:
        return open(CB_PATH, perm)
    except IOError:
        create_empty()
        return open(CB_PATH, perm)

def create_empty():
    with open(CB_PATH, 'w+') as f:
        pickle.dump([], f)
    if os.name == 'nt' or platform.system() == 'Windows':
        import win32con, win32api
        win32api.SetFileAttributes(CB_PATH, win32con.FILE_ATTRIBUTE_HIDDEN)

def load_cb():
    with open_cb("rb") as f:
        return pickle.load(f)

def save_cb(cb):
    with open_cb("wb") as f:
        pickle.dump(cb, f)

def push():
    cb = load_cb()
    if len(cb) > CB_SIZE:
        cb.pop(0)
    cb.append(getcb())
    save_cb(cb)

def pop():
    cb = load_cb()
    if len(cb) > 0:
        setcb(cb.pop())
    save_cb(cb)

def empty():
    save_cb([])

registered = {
    "push": push,
    "pop": pop,
    "empty": empty
    }

if __name__ == '__main__':
    _, cmd = sys.argv
    if cmd in registered:
        registered[cmd]()
