from .. import ui
from .raw_input_mocker import rawinput
ui.raw_input = rawinput
def test_prompt():
    assert ui.prompt("testing") == "test"

def test_get_details():
    assert ui.get_details()==('test','test','test','test','test')
