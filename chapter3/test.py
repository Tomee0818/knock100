s = "a b c https:/japan.jp "

start = s.index('ht')
end = s.index('p')
captured = s[start:end]

print(captured)