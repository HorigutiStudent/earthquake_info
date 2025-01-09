#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import argparse

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    talker = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'talker',
            )
    #テスト用
    
    listener = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'listener',
            output = 'screen',
            )

    return launch.LaunchDescription([talker,listener])


