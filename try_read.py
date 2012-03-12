f = file('p_text_1.txt')
string = f.read()
f2 = file('p_text_1.copy.txt', 'w')
for c in string:
    f2.write(c)
