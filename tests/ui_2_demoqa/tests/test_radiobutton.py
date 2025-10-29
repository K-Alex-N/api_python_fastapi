import pytest


@pytest.mark.parametrize(
    "value,expected_text",
    [
        ("yes", "Yes"),
        ("impressive", "Impressive"),
    ],
)
def test_radio_button_selection(radio_button_page, value, expected_text):
    radio_button_page.select(value)
    output = radio_button_page.get_output()
    assert output == expected_text
