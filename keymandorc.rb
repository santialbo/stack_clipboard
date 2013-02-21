start_at_login(true)

map "<Cmd-c>" do
    send("<Cmd-c>")
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py push`
end

map "<Shift-Cmd-v>" do
    send("<Cmd-v>")
    `/Users/santialbo/Developer/stack-clipboard/stack-clipboard.py pop`
end