#!/bin/bash

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws/src
git clone git@github.com:HorigutiStudent/Earthquake_msg.git
cd $dir/ros2_ws
colcon build
source $dir/.bashrc
# source /opt/ros/humble/setup.bash
source $dir/ros2_ws/install/setup.bash
pwd
# timeout 5 ros2 launch earthquake_info test.launch.py | tee - /tmp/earthquake_info.log

# cat /tmp/earthquake_info.log
# cat /tmp/earthquake_info.log | grep 'published 1:'

