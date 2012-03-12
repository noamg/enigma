
from trace import trace

import core_4
enigma_1 = core_4.enigma()
enigma_1.configure()
print 'intreactive enigma'

while True:
    char = raw_input()
    if char == 'quit':
        break
    assert(char != '\n') # for some reason, the last char in the file is <CR>, but it doen't appear in a text editor
    assert(int(char) in enigma_1.alphabet)
    p_num = int(char)
    trace(p_num, '>>>>>>>>>>>')
    e_num = enigma_1.click(p_num)
    trace(e_num, '>>>>>>>>>>>')
#    e_char = chr(e_num)
    print e_num
