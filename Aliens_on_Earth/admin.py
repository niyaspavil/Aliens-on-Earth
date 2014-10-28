

__plugins_dir__=os.path.dirname(os.path.abspath(__file__))+"/plugins"

class Aliens(object):
    def __init__(self,code_name,blood_color,no_of_antennas,no_of_legs,home_planet):
        self.code_name = code_name
        self.blood_color=blood_color
        self.no_of_antennas=no_of_antennas
        self.no_of_legs=no_of_legs
        self.home_planet=home_planet
    def __str__ (self):
        return self.code_name



def register(details):
    alien = Aliens(details)
    
