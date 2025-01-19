#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
     get_info = launch_ros.actions.Node(
         package='earthquake_info',
         executable='get_info',
         )
     listener = launch_ros.actions.Node(
         package='earthquake_info',
         executable='listener',
         output='screen'
                  )
     return launch.LaunchDescription([get_info, listener])