import random

from faker import Faker

fake = Faker()


class Payloads:
    create_category = {
        "name": fake.name(),
        "type": random.choice(["income", "expense"])
    }
