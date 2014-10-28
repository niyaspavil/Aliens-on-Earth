from .. import Terminal_ui
from .raw_input_mocker import rawinput
.raw_input = rawinput
def test_prompt():
    assert get_details.prompt("test") == "test"
