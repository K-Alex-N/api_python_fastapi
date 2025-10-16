import random
from typing import Any

from faker import Faker

fake = Faker()


class Payloads:
    @staticmethod
    def category() -> dict[str, str]:
        return {"name": fake.name(), "type": random.choice(["income", "expense"])}

    def _modified_category(self, *, drop=None, overrides=None) -> dict[str, Any]:
        payload = self.category()
        if drop:
            for key in drop:
                payload.pop(key, None)
        if overrides:
            payload.update(overrides)
        return payload

    def category_without_name(self) -> dict[str, Any]:
        return self._modified_category(drop=["name"])

    def category_without_type(self) -> dict[str, Any]:
        return self._modified_category(drop=["type"])

    def category_without_name_and_type(self) -> dict[str, Any]:
        return self._modified_category(drop=["name", "type"])

    def category_with_wrong_name(self) -> dict[str, Any]:
        return self._modified_category(overrides={"name": fake.pyint()})

    def category_with_wrong_type(self) -> dict[str, Any]:
        return self._modified_category(overrides={"type": "wrong_type"})


payloads = Payloads()
