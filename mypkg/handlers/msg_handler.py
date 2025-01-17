#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT


from earthquake_msg.msg import Earthquake
import time

# class MsgHandler:
#     def __init__(self):       
#         self.msg = Earthquake()
#         self.msgs = [
#           self.msg.datetime,
#           self.msg.epicentre,
#           self.msg.max_seismic,
#           self.msg.prefecture,
#           self.msg.city,
#           self.msg.magnitude,
#           self.msg.tunami,
#         ]
        
        
#     def send_msg(self,data_list:list) -> Earthquake:
#         for i in range(len(self.msgs)):
#             try:
#                 if i == 2:
#                     data_list[i] = self.__convert_type(data_list[i])
#                 elif i == 5:
#                     data_list[i] = self.__convert_type(data_list[i])
#                 self.msgs[i] = data_list[i]
#             except:
#                 self.msgs[i] = "none"
#         print(self.msg.datetime)
#         time.sleep(1)
#         print("-----------")
#         return self.msg
      
class MsgHandler:
    def __init__(self):
        self.msg = Earthquake()


    def send_msg(self, data_list: list) -> Earthquake:
        # try:
        self.msg.datetime = data_list[0]
        self.msg.epicentre = data_list[1]
        self.msg.max_seismic = self.__convert_type(data_list[2], "int")
        self.msg.prefecture = data_list[3]
        self.msg.city = data_list[4]
        self.msg.magnitude = self.__convert_type(data_list[5], "float")
        self.msg.tunami = data_list[6]
        # except (IndexError, ValueError) as e:
        #     print(f"Error updating message: {e}")
        return self.msg
      
            
    def __convert_type(self,val:any,to_:str="int"):
        if to_ == "int":
            try:
                return int(val)
            except:
                return 0
        elif to_ == "float":
            try:
                return float(val)
            except:
                return float(0)
          
if __name__ == "__main__":
    handler = MsgHandler()
    data = ["2025-01-17T21:11:43", "Tokyo", 7, "Tokyo", "Shibuya", 7.5, "None"]
    msg = handler.send_msg(data)
    print(msg)