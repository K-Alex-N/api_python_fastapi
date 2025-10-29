import os

import pytest
from playwright.sync_api import sync_playwright

from tests.ui_2_demoqa.pages.buttons_page import ButtonsPage
from tests.ui_2_demoqa.pages.checkbox_page import CheckboxPage
from tests.ui_2_demoqa.pages.radiobutton_page import RadioButtonPage
from tests.ui_2_demoqa.pages.textbox_page import TextBoxPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        headless_env = os.getenv("HEADLESS", "true").lower()
        headless = headless_env in ("1", "true", "yes", "on")
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def buttons_page(page):
    obj = ButtonsPage(page)
    obj.goto()
    return obj


@pytest.fixture
def checkbox_page(page):
    obj = CheckboxPage(page)
    obj.goto()
    obj.expand_all()
    return obj


@pytest.fixture
def radio_button_page(page):
    obj = RadioButtonPage(page)
    obj.goto()
    return obj


@pytest.fixture
def textbox_page(page):
    obj = TextBoxPage(page)
    obj.goto()
    return obj
