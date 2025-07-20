from tests.api_new.services.categories.api import CategoriesAPI


class TestCategories(CategoriesAPI):

    # @pytest.mark.skip
    def test_create_category(self):
        self.create_category()

    # @pytest.mark.skip
    def test_create_category_with_wrong_type(self):
        pass

    #     @pytest.mark.skip
    def test_get_category_by_id(self):
        category = self.create_category()
        self.get_category_by_id(category.id)

    #     @pytest.mark.skip
    def test_get_category_by_wrong_id(self):
        pass

    #     @pytest.mark.skip
    def test_get_all_categories(self):
        self.create_category()
        self.get_all_categories()

    # @pytest.mark.skip
    def test_update_category(self):
        category = self.create_category()
        self.update_category(category.id)

    def test_delete_category(self):
        category = self.create_category()
        self.delete_category(category.id)
