#!/bin/bash
#set -e

#dockerize -wait tcp://my-api-server:8000 -timeout 60s \

#echo "--- Запуск тестов для test_categories ---"
#pytest tests/api/tests/test_categories
#echo "--- Тесты для test_categories завершены ---"
#
#echo "--- Запуск тестов для test_transactions ---"
#pytest tests/api/tests/test_transactions
#echo "--- Тесты для test_transactions завершены ---"
pytest
#pytest -n 3
#pytest -n 4
#pytest -n 6
#pytest -n 8

sleep infinity

"$@"

