import os
from .. import admin

def test_Aliens():
    details = ('test_name',' test_color','1','2','test_planet')
    alien = admin.Aliens(details)
    assert alien.code_name == 'test_name'
    assert alien.home_planet == 'test_planet'


def test_get_format():
    __plugins_dir__=os.path.dirname(os.path.abspath(__file__))+"/plugins"
    assert admin.get_formats () == ['pdf','text_file']
