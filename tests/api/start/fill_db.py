from tests.api.services.categories.api import CategoriesAPI
from tests.api.services.transactions.api import TransactionsAPI

category = CategoriesAPI()
transaction = TransactionsAPI()

NUM_CATEGORIES = 3
NUM_TRANSACTIONS = 3

for _ in range(NUM_CATEGORIES):
    category.create_category()

for _ in range(NUM_CATEGORIES):
    transaction.create_transaction()
