#!/usr/bin/python
from pyperclip import setcb, getcb
import pickle
import sys, os

cb_path = os.path.join(os.path.expanduser("~"), ".clipboard")

def open_cb(perm):
    try:
        f = open(cb_path, perm)
        return f
    except IOError:
        f = open(cb_path, 'w+')
        pickle.dump([], f)
        f.close()
        f = open(cb_path, perm)
        return f

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
    if len(cb) > 0:
        cb.pop()
        if len(cb) > 0:
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
