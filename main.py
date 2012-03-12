"""
this is a wrapper around the enigma core.
get a path of a file as an argument
p___ - plain text, e___ - encripted.
"""
# determine - numbers or letters. - - todo.

from trace import trace

import sys
import os.path
import core_4

# set I/O
ptext_path = sys.argv[1]
etext_path = os.path.join("%s.encripted.txt" % ptext_path)
f_ptext = file(ptext_path)
ptext = f_ptext.read()
f_etext = file(etext_path, 'w')

enigma_1 = core_4.enigma()
enigma_1.configure()
enigma_1.shift = shift_user = sys.argv[2]

# protector
if ptext[-1] == '\n':
    ptext = ptext[:-1]

# calling the enigma function from the core, using the parameters from the conf, passing the result to the output file.
for char in ptext:
    assert(char != '\n') # for some reason, the last char in the file is <CR>, but it doen't appear in a text editor
    assert(int(char) in enigma_1.alphabet)
    p_num = int(char)
    trace(p_num, '>>>>>>>>>>>')
    e_num = enigma_1.click(p_num)
    trace(e_num, '>>>>>>>>>>>')
#    e_char = chr(e_num)
    e_char = str(e_num)
    f_etext.write(e_char)
