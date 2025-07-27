import random

from faker import Faker

fake = Faker()

class Payloads:

    @staticmethod
    def category():
        return {
            "name": fake.name(),
            "type": random.choice(["income", "expense"])
        }

    def category_without_name(self):
        payload = self.category()
        del payload["name"]
        return payload

    def category_without_type(self):
        payload = self.category()
        del payload["type"]
        return payload

    def category_without_name_and_type(self):
        payload = self.category()
        del payload["type"]
        del payload["name"]
        return payload

    def category_with_wrong_name(self):
        payload = self.category()
        payload["name"] = fake.pyint() # should be str
        return payload

    def category_with_wrong_type(self):
        payload = self.category()
        payload["type"] = "wrong_type" # should be only "income" or "expense"
        return payload

payloads = Payloads()