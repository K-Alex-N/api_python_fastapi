import random

from faker import Faker

fake = Faker()


def category_payload():
    return {
        "name": fake.name(),
        "type": random.choice(["income", "expense"])
    }
