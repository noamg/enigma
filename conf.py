"""
this is the enigma machine configuration script. - - - acctually, function definitions for conf.
upload the rotors
asserts that they are ok.
determine the number of the letters.
calculate the reverse rotors
upload plugboard.
assert that gluboard is ok.
determine initial rotors shift
"""

from trace import trace

def reverse_rotor(rotor):
    ''' returns the reverse list'''
    reverse = [None,] * len(rotor)
    for i in range(len(rotor)):
        reverse[rotor[i]] = i
   # assertion. question - is it better to assert once the entire vector is constructed? or every cell during the construction?
    for i in range(len(rotor)):
        assert(reverse[rotor[i]] == i)
    return reverse


def rotors():
    ''' fetch rotors from file and check them, reverse them ''' 
    import rotors_file
    rotors_no_reverse = rotors_file.rotors
    rotors = {}
 
    alpha_len = len(rotors_no_reverse[0])
    alphabet = range(alpha_len)
    for r in rotors_no_reverse.values(): 
        r_clone = r[:]
        r_clone.sort()
        assert(r_clone == alphabet)
 
    for i in range(len(rotors_no_reverse)):
        rotors[i] = rotors_no_reverse[i]
        rotors[-i] = reverse_rotor(rotors[i])
    return rotors

def shift():
    ''' return the rotors shift  - - - this is a mockup!!!!! '''
    shift = [0] * len(rotors()) # or maybe shift = sys.argv[2]
    return shift

def plugboard():
    ''' '''
    import plugboard
    return plugboard.plugboard
