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

payload = Payloads()