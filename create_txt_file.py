import random
from trace import trace
char_nam = int(argv[2])
trace(char_num)
path = argv[1]
trace(path)
file_1 = file(path, 'w')

for i in xrange(char_num):
    file_1.write(random.randint(0,3)
