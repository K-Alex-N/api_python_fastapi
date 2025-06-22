import allure


@allure.epic("UI")
@allure.feature("Inventory")
class TestInventory:
    def test_products_sort_by_name_from_a_to_z(self, inventory_page):
        # by default sort order is 'Name (A to Z)'
        inventory_page.is_products_sorted_by_name_from_a_to_z()

    def test_products_sort_by_name_from_z_to_a(self, inventory_page):
        inventory_page.set_sort_order("Name (Z to A)")
        inventory_page.is_products_sorted_by_name_from_z_to_a()

    def test_products_sort_by_price_from_low_to_high(self, inventory_page):
        inventory_page.set_sort_order("Price (low to high)")
        inventory_page.is_products_sorted_by_price_from_low_to_high()

    def test_products_sort_by_price_from_high_to_low(self, inventory_page):
        inventory_page.set_sort_order("Price (high to low)")
        inventory_page.is_products_sorted_by_price_from_high_to_low()


# def test_cart_bage_work
# спросить у Джипити как назвать функицю
# как назвать функцию которая проверяет работу бэйджа у корзины. В тесте будет проверяться что бэйдж увеличивается или уменьшается если добавлять больше товаров в корзину
