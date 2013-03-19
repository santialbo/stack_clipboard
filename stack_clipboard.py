#!/usr/bin/python
"""
stack_clipboard is a persistent stack clipboard system which allows to save the
content of the clipboard and retrieve it later by poping it.
"""
import pyperclip
import pickle
import sys, os, platform

CB_PATH = os.path.join(os.path.expanduser("~"), ".clipboard")
CB_SIZE = 100

def open_cb(perm):
    """ Returns the file handler for the clipboard storage file.  """
    try:
        return open(CB_PATH, perm)
    except IOError:
        create_empty()
        return open(CB_PATH, perm)

def create_empty():
    """ Creates an empty clipboard storage file. """
    with open(CB_PATH, 'w+') as handler:
        pickle.dump([], handler)
    if os.name == 'nt' or platform.system() == 'Windows':
        import win32con, win32api
        win32api.SetFileAttributes(CB_PATH, win32con.FILE_ATTRIBUTE_HIDDEN)

def load_cb():
    """ Returns the contents of the clipboard file as a list. """
    with open_cb("rb") as handler:
        return pickle.load(handler)

def save_cb(clipboard):
    """ Savves the given clipboard list in the storage file. """
    with open_cb("wb") as handler:
        pickle.dump(clipboard, handler)

def push():
    """ Pushes the content of the clipboard to the stack and saves it. """
    clipboard = load_cb()
    if len(clipboard) > CB_SIZE:
        clipboard.pop(0)
    clipboard.append(pyperclip.getcb())
    save_cb(clipboard)

def pop():
    """ Pops the stack. """
    clipboard = load_cb()
    if len(clipboard) > 0:
        pyperclip.setcb(clipboard.pop())
    save_cb(clipboard)

def empty():
    """ Empties the stack. """
    save_cb([])

COMMANDS = {
    "push": push,
    "pop": pop,
    "empty": empty
    }

if __name__ == '__main__':
    _, cmd = sys.argv
    if cmd in COMMANDS:
        COMMANDS[cmd]()
