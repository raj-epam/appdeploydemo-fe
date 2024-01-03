#!/bin/sh
snyk container test dhlawowacr.azurecr.io/pywebapp:$1  --file=./Dockerfile --json-file-output=vulnerabilities.json --org=raj-epam --project-name=python_demo-FE