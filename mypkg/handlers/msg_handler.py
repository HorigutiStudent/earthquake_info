#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT


from earthquake_msg.msg import Earthquake


class MsgHandler:
    def __init__(self):       
        self.msg = Earthquake()
        self.msgs = [
          self.msg.datetime,
          self.msg.epicentre,
          self.msg.max_seismic,
          self.msg.prefecture,
          self.msg.city,
          self.msg.magnitude,
          self.msg.tunami,
        ]
        
        
    def send_msg(self,data_list:list) -> Earthquake:
        for i in range(len(self.msgs)):
            try:
                if i == 2:
                    data_list[i] = self.__convert_type(data_list[i])
                elif i == 5:
                    data_list[i] = self.__convert_type(data_list[i])
                self.msgs[i] = data_list[i]
            except:
                continue
        return self.msg
      
      
    def __convert_type(val:any,to_:str="int"):
        if to_ == "int":
            return int(val)
        elif to_ == "float":
            return float(val)