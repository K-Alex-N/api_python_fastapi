import pytest

from .buttons_page import ButtonsPage


@pytest.fixture
def buttons_page_obj(page):
    obj = ButtonsPage(page)
    obj.goto()
    return obj


def test_double_click_button(buttons_page_obj):
    buttons_page_obj.double_click()
    assert "You have done a double click" in buttons_page_obj.double_click_msg()


def test_right_click_button(buttons_page_obj):
    buttons_page_obj.right_click()
    assert "You have done a right click" in buttons_page_obj.right_click_msg()


def test_dynamic_click_button(buttons_page_obj):
    buttons_page_obj.dynamic_click()
    assert "You have done a dynamic click" in buttons_page_obj.dynamic_click_msg()
