import allure


@allure.epic("UI")
@allure.feature("Inventory")
class TestInventory:
    def test_if_items_sorted_from_a_to_z(self, inventory_page):
        # by default sort order is 'Name (A to Z)'
        inventory_page.is_items_sorted_from_a_to_z()

    def test_if_items_sorted_from_z_to_a(self, inventory_page):
        inventory_page.set_sort_order("Name (Z to A)")
        inventory_page.is_items_sorted_from_z_to_a()

    # def test_if_


# Price (low to high)
# Price (high to low)

# def test_cart_bage_work
# спросить у Джипити как назвать функицю
# как назвать функцию которая проверяет работу бэйджа у корзины. В тесте будет проверяться что бэйдж увеличивается или уменьшается если добавлять больше товаров в корзину
