#!/bin/bash

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source $dir/ros2_ws/install/setup.bash
timeout 5 ros2 launch earthquake_info test.launch.py > /tmp/earthquake_info.log

cat /tmp/earthquake_info.log
cat /tmp/earthquake_info.log | grep 'published 1:'

