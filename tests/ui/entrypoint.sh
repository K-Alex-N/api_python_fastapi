#!/bin/bash
set -e

echo "Running tests..."
pytest --alluredir=/app/allure-results "$@"

#echo "Sending reports by email and Telegram..."
#python /app/send_report.py
