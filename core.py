"""
gets many variables from the ocnfiguratoin file:
    rotors
    initial rotors shit
    pluboard
    ALPHABET
    alpha_len
"""

from trace import trace

class enigma(object):
    """ machine state. shift of the rotors.
    attributes:
        rotors = a dict num:rotor. rotor is a list that maps numbers 0...n > 0....n
        shift = a list, the position of each rotor.
        rotors number
        alpha_len
        plugboard = is not implemented yet.
        ALPHBET"""

    attributes = ['rotors', 'shift', 'plugboard']
    #extra_attributes = [rotors_num, alpha_len, alphabet]
    def __init__(self, rotors = {}, shift = [], rotors_num = 0, alpha_len = 0, plugboard = [], alphabet = []):
        self.rotors = rotors
        self.shift = shift
        self.rotors_num = rotors_num
        self.alpha_len = alpha_len
        self.plugboard = plugboard
        self.alphabet = alphabet
    def calculate_extra_attributes(self):
        ''' use rotors to calc rotors_num, alphabet, alpha_leb '''
        self.rotors_num = (len(self.rotors) + 1 ) / 2
        self.alpha_len = len(self.rotors[0]) # check rotors length
        self.alphabet = range(self.alpha_len)
    def configure(self):   # could be more orthogonal : conf_file = conf_3.py
        ''' the enigma gets it's attributes from the conf file '''
        import conf_3
        # maybe more efficiant: for att in enigma.attributes:
            # self.att = conf_3.att()
        self.rotors = conf_3.rotors()
        self.shift = conf_3.shift()
        trace(self.shift)
        self.plugboard = conf_3.plugboard()


        self.calculate_extra_attributes()
    def rotate_one_rotor(self, rotor_num):
        """rotate one rotor forward """
        if rotor_num == 0:
            return
        else:
            self.shift[rotor_num] += 1
            self.shift[rotor_num] = self.shift[rotor_num] % self.alpha_len
            return

    def rotate(self):
        """ rotate each rotor, if needed"""
        self.rotate_one_rotor(self.rotors_num - 1)
        for i in range(self.rotors_num - 2, 0, -1):
            if self.shift[i + 1] == 0:
                self.rotate_one_rotor(i)
            else:
                break

        return self


    def sub_by_rotor(self, rotor_num, num):
        """ substitute the number by one rotor"""
        trace(num, '>')
        assert num in self.alphabet
        num += self.shift[rotor_num]
        num = num % self.alpha_len
        num = self.rotors[rotor_num][num]
        num -= self.shift[rotor_num]
        num = num % self.alpha_len
        trace(num, '>')
        return num

    def sub_by_all_rotors(self, num):
        """ substitute the number by all the rotors """
        for i in range(self.rotors_num - 1, -(self.rotors_num - 1), -1):
            num = self.sub_by_rotor(i, num)
        return num


    def sub_plugboard(self, num):
        """ substitute the number using the pkugboard """
        pass

    def click(self, p_num):
        """ this is the main enigma function: encript a letter and rotate the rotors """
        e_num = self.sub_by_all_rotors(p_num)
        self.rotate()
        return e_num
