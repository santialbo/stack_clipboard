start_at_login(true)

map "<Cmd-c>" do
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py push`
    send("<Cmd-c>")
end

map "<Shift-Cmd-v>" do
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py pop`
    send("<Cmd-v>")
end