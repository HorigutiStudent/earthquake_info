#!/usr/bim/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import argparse
import time

import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int16

from earthquake_info.handlers.data_handler import DataConfig,DataHandler
from earthquake_info.handlers.json_handler import JsonHandler
from earthquake_info.handlers.msg_handler  import MsgHandler

from earthquake_msg.msg import Earthquake


class Talker(Node):
    def __init__(self,data_config:DataConfig):
        super().__init__("talker")
        self.pub = self.create_publisher(Earthquake,"countup",10)
        self.create_timer(1,self.cb)
        self.data_config = data_config
        self.json_handler = JsonHandler()
        self.data_handler = DataHandler(self.data_config)
        self.msg_handler  = MsgHandler()        
        self.data_url = "https://www.jma.go.jp/bosai/quake/data/list.json"


    def cb(self):
        data_list = self.get_data()
        msg = self.msg_handler.send_msg(data_list)
        self.pub.publish(msg)
        
        
    def get_data(self) -> None:
        data = self.json_handler.parse(self.data_url)
        json_url = "https://www.jma.go.jp/bosai/quake/data/" + data[0]["json"]
        specific_data = self.json_handler.parse(json_url)
        data_list = self.data_handler.get_data(specific_data)
        return data_list        


def main(args=None):
    # ユーザーからの入力を入れる
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--city',
        default='false',
        help='最大震度観測地点を知りたい場合にセットする'
    )
    arg_parser.add_argument(
        '--magnitude',
        default='false',
        help='マグニチュードを知りたい場合にセットする'
    )
    arg_parser.add_argument(
        '--tunami',
        default='false',
        help='津波情報を知りたい場合にセットする'
    )

    args, other_args = arg_parser.parse_known_args(args)
    data_config = DataConfig(
        city=args.city.lower() == 'true',
        magnitude=args.magnitude.lower() == 'true',
        tunami=args.tunami.lower() == 'true'
    )
    rclpy.init(args=other_args)
    node = Talker(data_config)
    rclpy.spin(node)
