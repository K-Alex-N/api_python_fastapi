class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    def wait_for(self, selector, timeout=5000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def check_exists(self, selector):
        return self.page.locator(selector).count() > 0
