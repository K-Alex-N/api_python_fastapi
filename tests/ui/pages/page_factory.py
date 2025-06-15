from .login_page import LoginPage

class PageFactory:
    def __init__(self, page):
        self.page = page

    def get_page(self, page_name: str):
        match page_name.lower():
            case "login":
                return LoginPage(self.page)
            # Добавляй другие страницы здесь
            case _:
                raise ValueError(f"Page '{page_name}' not found in factory.")
