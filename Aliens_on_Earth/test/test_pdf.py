from .. plugins import pdf
from . alien_mocker import Aliens

alien = Aliens()

def test_create():
    temp_format = pdf.Pdf(alien)
    assert temp_format.create() == True
