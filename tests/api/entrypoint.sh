#!/bin/bash
set -e

dockerize -wait tcp://my-api-server:8000 -timeout 60s \

#pytest
#pytest -n 2
#pytest -n 3
#pytest -n 4
#pytest -n 6
#pytest -n 8

sleep infinity

#"$@"

