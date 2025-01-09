#!/bin/bash
#TODO : SPDX License 

dir=/home/akage/practice
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws
dir=~
colcon build
source $dir/.bashrc
timeout 3 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Lis: 0'


