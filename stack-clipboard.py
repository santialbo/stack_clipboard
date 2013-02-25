#!/usr/bin/python
from pyperclip import setcb, getcb
import pickle
import sys, os

CB_PATH = os.path.join(os.path.expanduser("~"), ".clipboard")

def open_cb(perm):
    try:
        return open(CB_PATH, perm)
    except IOError:
        with open(CB_PATH, 'w+') as f:
            pickle.dump([], f)
        return open(CB_PATH, perm)

def load_cb():
    with open_cb("rb") as f:
        return pickle.load(f)

def save_cb(cb):
    with open_cb("wb") as f:
        pickle.dump(cb, f)

def push():
    cb = load_cb()
    cb.append(getcb())
    save_cb(cb)

def pop():
    cb = load_cb()
    if len(cb):
        setcb(cb.pop())
    save_cb(cb)

def empty():
    save_cb([])

registered = {"push": push,
              "pop": pop,
              "empty": empty}

if __name__ == '__main__':
    _, cmd = sys.argv
    if cmd in registered:
        registered[cmd]()
