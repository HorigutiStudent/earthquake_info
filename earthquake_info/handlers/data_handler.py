#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

from dataclasses import dataclass,asdict


@dataclass
class DataConfig:
    """
    どの情報を入手するかを一括管理するためのクラス
    選択肢を追加するならDtaHandlerのfunctionsにも追加する
    """
    datetime:     bool = True  #日時
    epicentre:    bool = True  #震源地
    max_seismic:  bool = True  #最大震度
    prefecture:   bool = True  #震源地-県名
    city:         bool = False #震源地-市名
    magnitude:    bool = False #マグニチュード
    tunami:       bool = False #津波情報
    
    
class DataHandler:
    def __init__(self,data_config:DataConfig):
        self.data_config = data_config
        self.functions = [
          self.__get_datetime,
          self.__get_epicentre,
          self.__get_max_seismic,
          self.__get_prefecture,
          self.__get_city,
          self.__get_magnitude,
          self.__get_tunami,
        ]
        self.data = None
    
    
    def get_data(self,data) -> list:
        self.data = data
        # return self.__get_tunami()
        data_list = ["none" for _ in range(len(self.functions))]
        config_dict = asdict(self.data_config)
        for i,val in enumerate(config_dict.values()):
            if val is True:
                data_list[i] = (self.functions[i]())
        return data_list
        
          
    def updtae_config(self,data_config:DataConfig) -> None:
        self.data_config = data_config
      
        
    def __get_datetime(self) -> str:
        return self.data["Body"]["Earthquake"]["OriginTime"]
      
    def __get_epicentre(self) -> str:
        return self.data["Body"]["Earthquake"]["Hypocenter"]["Area"]["Name"]
      
    def __get_max_seismic(self) -> str:
        return self.data["Body"]["Intensity"]["Observation"]["MaxInt"]
      
    def __get_prefecture(self) -> str:
        return self.data["Body"]["Intensity"]["Observation"]["Pref"][0]["Name"]
      
    def __get_city(self) -> str:
        return self.data["Body"]["Intensity"]["Observation"]["Pref"][0]["Area"][0]["City"][0]["Name"]
      
    def __get_magnitude(self) -> str:
        return self.data["Body"]["Earthquake"]["Magnitude"]
      
    def __get_tunami(self) -> str:
        return self.data["Body"]["Comments"]["ForecastComment"]["Text"]
      
      
if __name__ == "__main__":
    import sys
    sys.path.append("/home/akage/practice/ros2_ws/src/earthquake_info")
    from earthquake_info.handlers.json_handler import JsonHandler
    
    jsonhandler = JsonHandler()
    url = "https://www.jma.go.jp/bosai/quake/data/list.json"
    data = jsonhandler.parse(url)
    json_url =  "https://www.jma.go.jp/bosai/quake/data/" + data[0]["json"]
    specific_data = jsonhandler.parse(json_url)
    
    data_config = DataConfig()
    data_handler = DataHandler(data_config)
    date_time = data_handler.get_data(specific_data)
    print(date_time)