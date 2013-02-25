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
        cb.pop()
        if len(cb):
            setcb(cb[-1])
    save_cb(cb)

def empty():
    cb = []
    save_cb(cb)

if len(sys.argv) == 2:
    if sys.argv[1] == "push":
        push()
    elif sys.argv[1] == "pop":
        pop()
    elif sys.argv[1] == "empty":
        empty()
