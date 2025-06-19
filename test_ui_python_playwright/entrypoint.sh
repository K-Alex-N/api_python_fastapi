#!/bin/bash
set -e

mkdir "testttt"
copy -r .\app\ .\testttt


#echo "Running tests..."
#pytest --alluredir=/app/allure-results "$@"

#echo "Sending reports by email and Telegram..."
#python /app/_send_report.py
