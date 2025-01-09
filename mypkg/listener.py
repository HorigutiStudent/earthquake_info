#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.pub = self.create_subscription(Int16,"countup",self.cb,10)
        

    def cb(self,msg):
        self.get_logger().info("Lis: %d " % msg.data)


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

    
