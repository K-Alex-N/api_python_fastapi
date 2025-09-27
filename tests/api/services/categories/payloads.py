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

    def _modified_category(self, *, drop=None, overrides=None):
        payload = self.category()
        if drop:
            for key in drop:
                payload.pop(key, None)
        if overrides:
            payload.update(overrides)
        return payload

    def category_without_name(self):
        return self._modified_category(drop=["name"])

    def category_without_type(self):
        return self._modified_category(drop=["type"])

    def category_without_name_and_type(self):
        return self._modified_category(drop=["name", "type"])

    def category_with_wrong_name(self):
        return self._modified_category(overrides={"name": fake.pyint()})

    def category_with_wrong_type(self):
        return self._modified_category(overrides={"type": "wrong_type"})

payloads = Payloads()
