from .. plugins import text_file
from . alien_mocker import Aliens

alien = Aliens()

def test_create():
    temp_format = text_file.Text_File(alien)
    assert temp_format.create() == True
