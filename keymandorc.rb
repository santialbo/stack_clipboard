start_at_login(true)

map "<Cmd-c>" do
    send("<Cmd-c>")
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py push`
end

map "<Cmd-x>" do
    send("<Cmd-x>")
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py push`
end

map "<Shift-Cmd-v>" do
    send("<Cmd-v>")
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py pop`
end

map "<Shift-Alt-Cmd-v>" do
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py empty`
end