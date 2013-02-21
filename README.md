stack-clipboards
================
This is a persistent stack clipboard. 
* Calling `stack-clipboard.py push` pushes the current clipboard content into the stack which is stored in `~/.clipboard`.
* Calling `stack-clipboard.py pop` pops the top of the stack and sets the new top as the clipboard content.

Shortcut support
================
I've added support for [keymando](http://keymando.com/) in the following way:
* ⌘-c copies the selection and calls `stack-clipboard.py push`
* ⇧-⌘-v pastes the content in the clipboard and calls `stack-clipboard.py pop`
