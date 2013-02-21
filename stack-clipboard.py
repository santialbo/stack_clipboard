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
    f = open_cb("rb")
    cb = pickle.load(f)
    f.close()
    return cb

def save_cb(cb):
    f = open_cb("wb")
    pickle.dump(cb, f)
    f.close()

def push():
    cb = load_cb()
    cb.append(getcb())
    save_cb(cb)

def pop():
    cb = load_cb()
    if len(cb) > 1:
        cb.pop()
        setcb(cb[-1])
    save_cb(cb)


if len(sys.argv) == 2:
    if sys.argv[1] == "push":
        push()
    elif sys.argv[1] == "pop":
        pop()