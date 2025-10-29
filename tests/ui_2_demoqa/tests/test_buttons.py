

def test_double_click_button(buttons_page):
    buttons_page.double_click()
    assert "You have done a double click" in buttons_page.double_click_msg()


def test_right_click_button(buttons_page):
    buttons_page.right_click()
    assert "You have done a right click" in buttons_page.right_click_msg()


def test_dynamic_click_button(buttons_page):
    buttons_page.dynamic_click()
    assert "You have done a dynamic click" in buttons_page.dynamic_click_msg()
