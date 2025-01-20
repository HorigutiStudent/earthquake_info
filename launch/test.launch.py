#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import launch
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    declare_arg_city = DeclareLaunchArgument(
        'city', default_value='false',
        description='最大震度観測地点を知りたい場合にセットする'
    )

    declare_arg_magnitude = DeclareLaunchArgument(
        'magnitude', default_value='false',
        description='マグニチュードを知りたい場合にセットする'
    )

    declare_arg_tunami = DeclareLaunchArgument(
        'tunami', default_value='false',
        description='津波情報を知りたい場合にセットする'
    )

    get_info = Node(
        package='earthquake_info',
        executable='get_info',
        output='screen',
        arguments=[
            '--city', LaunchConfiguration('city'),
            '--magnitude', LaunchConfiguration('magnitude'),
            '--tunami', LaunchConfiguration('tunami')
        ]
    )

    listener = Node(
        package='earthquake_info',
        executable='listener',
        output='screen'
    )

    return launch.LaunchDescription([
        declare_arg_city,
        declare_arg_magnitude,
        declare_arg_tunami,
        get_info,
        listener
    ])
    
# def generate_launch_description():
#      get_info = launch_ros.actions.Node(
#          package='earthquake_info',
#          executable='get_info',
#          )
#      listener = launch_ros.actions.Node(
#          package='earthquake_info',
#          executable='listener',
#          output='screen'
#                   )
#      return launch.LaunchDescription([get_info, listener])