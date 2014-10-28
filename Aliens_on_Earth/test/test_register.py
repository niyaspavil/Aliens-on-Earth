from .. import register
from .raw_input_mocker import rawinput
register.raw_input = rawinput
def test_prompt():
    assert register.prompt("test") == "test"
