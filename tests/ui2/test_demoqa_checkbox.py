import pytest

from .checkbox_page import CheckboxPage


@pytest.fixture
def checkbox_page_obj(page):
    obj = CheckboxPage(page)
    obj.goto()
    obj.expand_all()
    return obj


@pytest.mark.parametrize(
    "check_node,expected_present,expected_absent",
    [
        ("home", ["home"], ["desktop", "documents", "downloads"]),
        ("desktop", ["desktop"], ["documents", "downloads"]),
    ],
)
def test_checkboxes_selection(
    checkbox_page_obj, check_node, expected_present, expected_absent
):
    checkbox_page_obj.select_checkbox(check_node)
    selected = checkbox_page_obj.get_selected_values()
    for value in expected_present:
        assert value in selected, (
            f"Expected '{value}' to be selected. Output: {selected}"
        )
    for value in expected_absent:
        assert value not in selected, (
            f"Did not expect '{value}' to be selected. Output: {selected}"
        )


def test_collapse_all_keeps_output_visible(checkbox_page_obj):
    checkbox_page_obj.select_checkbox("home")
    checkbox_page_obj.collapse_all()
    assert checkbox_page_obj.is_result_visible()
