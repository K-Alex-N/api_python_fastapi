import pytest

from .textbox_page import TextBoxPage


@pytest.fixture
def textbox_page_obj(page):
    obj = TextBoxPage(page)
    obj.goto()
    return obj


@pytest.mark.parametrize(
    "name,email,current_address,permanent_address",
    [
        ("Alice Test", "alice@example.com", "123 Main St", "456 Secondary Ave"),
    ],
)
def test_textbox_fields_output(
    textbox_page_obj, name, email, current_address, permanent_address
):
    textbox_page_obj.fill_form(name, email, current_address, permanent_address)
    textbox_page_obj.submit()
    output = textbox_page_obj.get_output_text()
    assert name in output
    assert email in output
    assert current_address in output
    assert permanent_address in output
