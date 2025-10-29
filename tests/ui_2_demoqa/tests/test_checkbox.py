import pytest


@pytest.mark.parametrize(
    "check_node,expected_present,expected_absent",
    [
        ("home", ["home", "desktop", "documents", "downloads"], []),
        ("desktop", ["desktop", "notes", "commands"], ["documents", "downloads"]),
    ],
)
def test_checkboxes_selection(
    checkbox_page, check_node, expected_present, expected_absent
):
    checkbox_page.select_checkbox(check_node)
    selected = checkbox_page.get_selected_values()
    for value in expected_present:
        assert value in selected, (
            f"Expected '{value}' to be selected. Output: {selected}"
        )
    for value in expected_absent:
        assert value not in selected, (
            f"Did not expect '{value}' to be selected. Output: {selected}"
        )


def test_collapse_all_keeps_output_visible(checkbox_page):
    checkbox_page.select_checkbox("home")
    checkbox_page.collapse_all()
    assert checkbox_page.is_result_visible()
