#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT


import requests

url = "https://www.jma.go.jp/bosai/quake/data/list.json"

response = requests.get(url)

data = response.json()

json_key = data[0]["json"]

print(json_key)