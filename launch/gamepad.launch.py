#===========================================================================
# Control robot using gamepad controller and RVIZ
#===========================================================================

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition


def generate_launch_description():
    use_local_gamepad = LaunchConfiguration('use_local_gamepad', default=true)

    package_name = 'hb_bot'

    gamepad_params_file = os.path.join(get_package_share_directory('hb_bot'),'config','gamepad.yaml')

    gamepad_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[gamepad_params_file],
        condition=IfCondition(use_local_gamepad)
    )

    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_node',
        parameters=[gamepad_params_file],
        remappings=[('/cmd_vel','/diff_cont/cmd_vel_unstamped')]
    )

    laser_filter_params_file = os.path.join(get_package_share_directory('hb_bot'),'config','laser_filter_param.yaml')

    laser_filter = Node(
        package='laser_filters',
        executable='scan_to_scan_filter_chain',
        name='laser_filter',
        parameters=[laser_filter_params_file] 
    )

    map_launch_file = os.path.join(get_package_share_directory(package_name),'launch','map.launch.py')

    return LaunchDescription([
        gamepad_node,
        teleop_node,
        laser_filter,        
        IncludeLaunchDescription( map_launch_file),       # SLAM map generator
    ])
    