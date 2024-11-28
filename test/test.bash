#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

dir="/home/RoboSys"
cd $dir/ros2_ws
./colbuild
source install/setup.bash
timeout 3 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | 
	grep 'Lis: 0'


