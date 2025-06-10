
# assert_schema_valid(response.json(), user_list_schema)

# def assert_schema_valid(что сравнить, с чем сравнить):
def assert_schema_valid(response):
    # проверить schema

    assert response.status_code == 200
    assert response.reason == "OK"
    assert isinstance(response.json(), list)