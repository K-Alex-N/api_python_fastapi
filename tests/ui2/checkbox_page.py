class CheckboxPage:
    URL = "https://demoqa.com/checkbox"

    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(self.URL)

    def expand_all(self):
        btn = self.page.locator("button[title='Expand all']")
        if btn.is_visible():
            btn.click()

    def collapse_all(self):
        btn = self.page.locator("button[title='Collapse all']")
        if btn.is_visible():
            btn.click()

    def select_checkbox(self, node):
        self.page.locator(f"label[for='tree-node-{node}'] span.rct-checkbox").click()

    def get_selected_values(self):
        result_text = self.page.locator("#result").inner_text()
        if ":" in result_text:
            return [
                item.strip().lower()
                for item in result_text.split(":", 1)[-1].split()
                if item != ""
            ]
        else:
            return []

    def is_result_visible(self):
        return self.page.locator("#result").is_visible()
