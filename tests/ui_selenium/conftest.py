# @pytest.fixture
# @pytest.mark.asyncio  !!!!!!!!!!!!!
# async def my_async_fixture():
#     print("\n--- Асинхронная фикстура: подготовка ---")
#     yield "async_data"
#     print("--- Асинхронная фикстура: очистка ---")
#
# @pytest.mark.asyncio
# async def test_with_async_fixture(my_async_fixture):
#     print(f"Использую данные из фикстуры: {my_async_fixture}")
#     assert my_async_fixture == "async_data"