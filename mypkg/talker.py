#!/usr/bim/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import argparse
import time

import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self,):
        super().__init__("talker")
        self.pub = self.create_publisher(Int16,"countup",10)
        self.create_timer(0.5,self.cb)
        self.n = 0


    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1


def main():
    #ユーザーからの入力を入れる
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
      '--region',
      default='none',
      type=str,
      help='地方を限定して取得する'
    )
    arg_parser.add_argument(
      '--prefecture',
      default='none',
      type=str,
      help='県を限定して取得する'
    )
    
    args,other_args = arg_parser.parse_known_args()
    print(args.region)
    raise KeyboardInterrupt
    rclpy.init(args=other_args)
    node = Talker()
    rclpy.spin(node)
    
    try:
        main()
    except KeyboardInterrupt:
        pass
      
    print("stop spin")
    time.sleep(1.0)
    
    pass
    # rclpy.init()
    # node = Talker()
    # rclpy.spin(node)


if __name__ == "__main__":
    #ユーザーからの入力を入れる
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
      '--region',
      default='none',
      type=str,
      help='地方を限定して取得する'
    )
    arg_parser.add_argument(
      '--prefecture',
      default='none',
      type=str,
      help='県を限定して取得する'
    )
    
    args,other_args = arg_parser.parse_known_args()
    print(args.region)
    #raise KeyboardInterrupt
    rclpy.init(other_args)
    node = Talker()
    rclpy.spin()
    
    try:
        main()
    except KeyboardInterrupt:
        pass
      
    print("stop spin")
    time.sleep(1.0)
    
    rclpy.shutdown()
    
