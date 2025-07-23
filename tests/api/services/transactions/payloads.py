from faker import Faker

from tests.api.services.categories.get_all_categories import GetAllCategories

fake = Faker()

class Payloads:

    @staticmethod
    def create_transaction(category_id: str = None) -> dict:
        return {
            "amount": fake.pyint(min_value=10, max_value=2000),
            "date": str(fake.date_time_between(start_date="-30d")),
            "description": fake.sentence(),
            # "category_id": GetAllCategories().get_random_category_id() #!!!!!!!!!!!!!!!!! тест прошел при закоментенной строчке. наверное ID создался в БД. проверить данные без Компас
        }





payloads = Payloads()