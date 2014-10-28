import os

__plugins_dir__=os.path.dirname(os.path.abspath(__file__))+"/plugins"

class Aliens(object):
    def __init__(self,details):
        self.code_name = details[0]
        self.blood_color=details[1]
        self.no_of_antennas=details[2]
        self.no_of_legs=details[3]
        self.home_planet=details[4]
    def __str__ (self):
        return self.code_name



def register(details):
    alien = Aliens(details)
    return True
