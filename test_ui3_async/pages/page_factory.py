# from .login_page import LoginPage
#
# class PageFactory:
#     def __init__(self, page):
#         self.page = page
#
#     def get_page(self, page_name: str):
#         match page_name.lower():
#             case "login":
#                 return LoginPage(self.page)
#             # Добавляй другие страницы здесь
#             case _:
#                 raise ValueError(f"Page '{page_name}' not found in factory.")

from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage

class PageFactory:
    def __init__(self, page):
        self.page = page

    def get_page(self, name: str):
        match name.lower():
            case "login":
                return LoginPage(self.page)
            case "inventory":
                return InventoryPage(self.page)
            case "cart":
                return CartPage(self.page)
            case _:
                raise ValueError(f"Page '{name}' not found")

