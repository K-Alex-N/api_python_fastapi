#!/bin/bash
#set -e


#mkdir .\tests\api2\tests\app\test_api
#copy -r .\app\ .\tests\api_2\

echo "Running tests..."
pytest --alluredir=/app/allure-results "$@"

#echo "Sending reports by email and Telegram..."
#python /app/_send_report.py



