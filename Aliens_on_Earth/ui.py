from . import admin
class Ui(object):
    def __init__(self):
        pass
    def get_details(self):
        print  '\n'+'\t'*3 +"Welcome to Registration.\n"
        code_name = self.prompt('Name code')
        blood_color =self. prompt('Blood color')
        no_of_antennas =self. prompt('Number of antennas')
        no_of_legs = self.prompt('Number of legs')
        home_planet = self.prompt('Home Planet')
        return (code_name,blood_color,no_of_antennas,no_of_legs,home_planet)


    def prompt(self,message):
        return raw_input('\n'+message+':- ')


def main():
    ui = Ui()
    details = ui.get_details()
    status = admin.register(details)
    if status == True:
        print "suceessfully registered"
    else:
        print "registration failed"

    


