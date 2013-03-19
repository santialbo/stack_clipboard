stack_clipboard
===============
stack_clipboard is a persistent stack clipboard system which allows to save the content of the clipboard and retrieve it later by poping it.
* `stack_clipboard.py push` pushes the current clipboard content into the stack which is stored in `~/.clipboard`.
* `stack_clipboard.py pop` pops the top of the stack and sets the new top as the clipboard content.
* `stack_clipboard.py empty` empties the stack.

Shortcut support
================
I've added support for [keymando](http://keymando.com/) in the following way:
* ⌘-c Pushes the current clipboard content into the stack copies the selection.
* ⌘-x Pushes the current clipboard content into the stack copies the selection.
* ⇧-⌘-v Pops the stack into the clipboard and pastes this new element
* ⇧-⌥-⌘-v Empties the stack calling.
