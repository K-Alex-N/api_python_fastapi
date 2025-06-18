import time

from test_ui2.pages.inventory_page import InventoryPage

def test_inventory(page):
    inventory_page = InventoryPage(page)
    inventory_page.open()

    # time.sleep(99)

# def test_cart_bage_work
# спросить у Джипити как назвать функицю
# как назвать функцию которая проверяет работу бэйджа у корзины. В тесте будет проверяться что бэйдж увеличивается или уменьшается если добавлять больше товаров в корзину


# сортировки обязательно проверить. там интересная логика должна быть