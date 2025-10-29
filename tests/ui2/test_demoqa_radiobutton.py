import pytest

from .radiobutton_page import RadioButtonPage


@pytest.fixture
def radio_button_page_obj(page):
    obj = RadioButtonPage(page)
    obj.goto()
    return obj


@pytest.mark.parametrize(
    "value,expected_text",
    [
        ("yes", "Yes"),
        ("impressive", "Impressive"),
    ],
)
def test_radio_button_selection(radio_button_page_obj, value, expected_text):
    radio_button_page_obj.select(value)
    output = radio_button_page_obj.get_output()
    assert output == expected_text
