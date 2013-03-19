start_at_login(true)

map "<Cmd-c>" do
    `/Users/santi/Developer/stack_clipboard/stack_clipboard.py push`
    send("<Cmd-c>")
end

map "<Cmd-x>" do
    `/Users/santi/Developer/stack_clipboard/stack_clipboard.py push`
    send("<Cmd-x>")
end

map "<Shift-Cmd-v>" do
    `/Users/santi/Developer/stack_clipboard/stack_clipboard.py pop`
    send("<Cmd-v>")
end

map "<Shift-Alt-Cmd-v>" do
    `/Users/santi/Developer/stack_clipboard/stack_clipboard.py empty`
end
