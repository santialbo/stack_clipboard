stack-clipboard
===============
This is a persistent stack clipboard. 
* Calling `stack-clipboard.py push` pushes the current clipboard content into the stack which is stored in `~/.clipboard`.
* Calling `stack-clipboard.py pop` pops the top of the stack and sets the new top as the clipboard content.
* Calling `stack-clipboard.py empty` creates a new stack and deletes the old one.

Shortcut support
================
I've added support for [keymando](http://keymando.com/) in the following way:
* ⌘-c Pushes the selection into the stack.
* ⌘-x Pushes the selection into the stack.
* ⇧-⌘-v pastes the content in the clipboard and calls `stack-clipboard.py pop`
* ⇧-⌥-⌘-v empties the stack calling `stack-clipboard.py empty`
