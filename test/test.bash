#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

dir="/home/RoboSys"
cd $dir/ros2_ws
./colbuild
source ~/.bashrc
timeout 3 ros2 launch mypkg talk_listen.launch.py > tee - /tmp/mypkg.log

cat /tmp/mypkg.log | 
	grep 'Lis: 0'


