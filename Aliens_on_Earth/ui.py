def get_details():
    print  '\n'+'\t'*3 +"Welcome to Registration.\n"
    code_name = prompt('Enter your name code:')
    blood_color = prompt('\nEnter your blood color:')
    no_of_antennas = prompt('\nEnter your number of antennas:')
    no_of_legs = prompt('\nEnter your number of legs:')
    home_planet = prompt('\nEnter your Home Planet:')
    return (code_name,blood_color,no_of_antennas,no_of_legs,no_of_planet)


def prompt(message):
   return raw_input(message)





