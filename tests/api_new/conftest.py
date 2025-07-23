# import pytest
#
# from tests.api_new.services.categories.create_category import CreateCategory
# from tests.api_new.services.categories.delete_category import DeleteCategory
# from tests.api_new.services.categories.get_all_categories import GetAllCategories
# from tests.api_new.services.categories.payloads import Payloads
# from tests.api_new.services.transactions.create_transaction import CreateTransaction
#
#
# @pytest.fixture(scope="session", autouse=True)
# def db_data_management():
#     # создаем новую БД
#
#     # Фикстура для подключения к MongoDB
#     @pytest.fixture(scope="session")  # Выполняется один раз за тестовую сессию
#     def mongo_client():
#         client = MongoClient("mongodb://localhost:27017/")
#         yield client
#         client.close()
#
#     # Фикстура для очистки базы данных перед каждым тестом
#     @pytest.fixture(autouse=True)  # Эта фикстура будет автоматически применяться ко всем тестам
#     def clean_db(mongo_client):
#         db_name = "test_db"
#         # Удаляем базу данных перед каждым тестом
#         mongo_client.drop_database(db_name)
#         print(f"\nБаза данных '{db_name}' очищена перед тестом.")
#         yield
#         # Опционально: можно добавить очистку после теста, если необходимо
#         # mongo_client.drop_database(db_name)
#         # print(f"База данных '{db_name}' очищена после теста.")
#
#     # Пример тестового файла (test_api.py)
#     def test_create_user(mongo_client):
#         db = mongo_client.test_db
#         users_collection = db.users
#         # Проверяем, что коллекция пуста
#         assert users_collection.count_documents({}) == 0
#
#         # Выполняем действия API, которые добавляют пользователя
#         users_collection.insert_one({"name": "Test User", "email": "test@example.com"})
#
#         # Проверяем результат
#         assert users_collection.count_documents({}) == 1
#         user = users_collection.find_one({"name": "Test User"})
#         assert user is not None
#
#     def test_get_empty_users(mongo_client):
#         db = mongo_client.test_db
#         users_collection = db.users
#         # После clean_db, коллекция должна быть пуста
#         assert users_collection.count_documents({}) == 0
#
# _______________
#
#
#     # create 2 categories and 2 transactions
#     cat = CreateCategory()
#     txn = CreateTransaction()
#
#     for _ in range(2):
#         cat.create_category(Payloads.category())
#         # txn.create_transaction(???)
#
#     yield
#     # clean db after tests
#     get_ll_cats = GetAllCategories()
#     cats = get_ll_cats.get_all_categories()
#     # cats = GetAllCategories().get_all_categories()
#
#     delete_cat = DeleteCategory()
#
#     for cat in cats.json():
#         delete_cat.delete_category(cat["id"])
#         # DeleteCategory().delete_category(cat["id"])
#
#     # еще удаление транзакций сделать
#
#     client = AsyncIOMotorClient(
#         MONGO_URL,
#     )
#     # if db == "test":
#     # else: print("you are trying to drop not test db")
#     db = client.test
#     db.