import os
import glob
from os.path import basename, splitext 
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



def register(details,ui):
    ui = ui
    alien = Aliens(details)
    all_format = get_formats()
    
    return True


def get_formats():
    """returns list of available channel/plugins by searching
    plugin directory"""
    formats = []
    format_files = glob.glob("{}/*.py".format(__plugins_dir__))
    for format_file in format_files:
        if format_file.endswith("__init__.py"):
            continue
        name, ext = splitext(basename(format_file))
        formats.append(name)
    return formats
