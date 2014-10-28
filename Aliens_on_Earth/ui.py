def get_details():
    print  '\n'+'\t'*3 +"Welcome to Registration.\n"
    code_name = prompt('Name code')
    blood_color = prompt('Blood color')
    no_of_antennas = prompt('Number of antennas')
    no_of_legs = prompt('Number of legs')
    home_planet = prompt('Home Planet')
    return (code_name,blood_color,no_of_antennas,no_of_legs,home_planet)


def prompt(message):
   return raw_input('\n'+message+':- ')


def main():
    details = get_details()
    return True
    


