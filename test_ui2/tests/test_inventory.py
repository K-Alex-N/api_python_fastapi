import time

import allure

from test_ui2.pages.inventory_page import InventoryPage


@allure.epic("UI")
@allure.feature("Inventory")
class TestInventoryPage:
    def test_inventory(self, inventory_page: InventoryPage):
        # inventory_page.
        pass




    # time.sleep(99)

# def test_cart_bage_work
# спросить у Джипити как назвать функицю
# как назвать функцию которая проверяет работу бэйджа у корзины. В тесте будет проверяться что бэйдж увеличивается или уменьшается если добавлять больше товаров в корзину


# сортировки обязательно проверить. там интересная логика должна быть
