#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import requests


class JsonHandler:
    def __init__(self):
        self.data = None
      
      
    def parse(self,url:str) -> any:
        response = requests.get(url)
        self.data = response.json()
        return self.data
      
      
if __name__ == "__main__":
    jsonhandler = JsonHandler()
    url = "https://www.jma.go.jp/bosai/quake/data/list.json"
    data = jsonhandler.parse(url)
    json_url =  "https://www.jma.go.jp/bosai/quake/data/" + data[0]["json"]
    print(json_url)
    specific_data = jsonhandler.parse(json_url)
    data_head = specific_data["Head"]
    data_body = specific_data["Body"]
    print(data_head)