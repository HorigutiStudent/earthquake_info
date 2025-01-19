#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import rclpy
from rclpy.node import Node

from earthquake_msg.msg import Earthquake

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.pub = self.create_subscription(Earthquake,"countup",self.cb,10)
        

    def cb(self,msg):
        self.get_logger().info(f'Publishing: {msg.datetime}, {msg.epicentre},{msg.max_seismic},{msg.prefecture},{msg.city},{msg.magnitude},{msg.tunami}')


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

    
