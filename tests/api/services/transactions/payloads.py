from faker import Faker

fake = Faker()


def payload_create_transaction(category_id: str = None) -> dict:
    payload = {
        "amount": fake.pyint(min_value=10, max_value=2000),
        "date": str(fake.date_time_between(start_date="-30d")),
        "description": fake.sentence(),
    }

    if category_id:
        payload["category_id"] = category_id

    return payload
