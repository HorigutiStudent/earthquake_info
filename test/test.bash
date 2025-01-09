#!/bin/bash

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 3 ros2 launch mypkg talk_listen.launch.py | tee -  /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Lis: 3'

