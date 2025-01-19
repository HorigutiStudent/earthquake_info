#!/bin/bash

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 run earthquake_info get_info | tee -  /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Lis: 3'

