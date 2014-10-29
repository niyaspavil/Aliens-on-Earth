class text_file(object):
    def __init__(self,alien):
        self.alien = alien
    
    def create(self):
        name = self.alien.code_name+'.txt'
        try:
            f = open(name,'w')
            f.write('Code Name:  ' + self.alien.code_name + '\n' +
                'Blood Color:' +self.alien.blood_color + '\n' +
                'No of Antennas:  '+self.alien.no_of_antennas + '\n' +
                'No of Legs:  '+self.alien.no_of_legs + '\n' +
                'Home Planet:  '+self.alien.home_planet 
                   )
            f.close()
        except exception as e:
            print e
        return True
