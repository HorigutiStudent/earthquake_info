#!/bin/bash

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

dir=~
[ "$1" != "" ] && dir="$1"
# cd $dir/ros2_ws/src
# git clone git@github.com:HorigutiStudent/earthquake_msg.git
source /opt/ros/humble/setup.bash

cd $dir/ros2_ws
colcon build
# source $dir/.bashrc


# source $dir/ros2_ws/install/setup.bash
# source $dir/ros2_ws/install/local_setup.bash

# ros2 pkg list | grep earth*
# # pwd ## /root/ros2_ws
# # ls src  # earthquake_msg
#         # earthquake_info

# #ls src/earthquake_info/earthquake_info

# timeout 5 ros2 launch earthquake_info test.launch.py | tee - /tmp/earthquake_info.log

# #cat /tmp/earthquake_info.log
# cat /tmp/earthquake_info.log | grep 'published 1:'

