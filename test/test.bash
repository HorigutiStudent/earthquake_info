#!/bin/bash

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

ng () {
    res = 1
}
test_package () {
    timeout 5s sh -c "
      ros2 launch earthquake_info test.launch.py ${1}
    "
}

dir=~
[ "$1" != "" ] && dir="$1"
source /opt/ros/humble/setup.bash

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# ros2 pkg list | grep earth*

res = 0

out=$( test_package city:=true )
[ "$?" = 0 ] || ng "$LINENO"

out=$( test_package magnitude:=true )
[ "$?" = 0 ] || ng "$LINENO"

out=$( test_package tunami:=true )
[ "$?" = 0 ] || ng "$LINENO"

#malformed launch argument 'city', expected format '<name>:=<value>'
out=$( test_package city )
[ "$?" = 1 ] || ng "$LINENO"

#入力ミスがあってもエラーは起こさない
out=$( test_package tnami:=true )
[ "$?" = 0 ] || ng "$LINENO"

timeout 5 ros2 launch earthquake_info test.launch.py city:=true magnitude:=true tunami:=true | tee - /tmp/earthquake_info.log

cat /tmp/earthquake_info.log | grep 'published 1:'

