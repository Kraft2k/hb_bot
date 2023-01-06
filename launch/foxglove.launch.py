#===========================================================================
# Control robot using foxglove and the gamepad controller
#===========================================================================

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition

use_local_gamepad = LaunchConfiguration('use_local_gamepad', default=True)
use_foxglove = LaunchConfiguration('use_foxglove', default=True)

def generate_launch_description():
 
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

    rosbridge_websocket_node = Node(
        package='rosbridge_server',
        executable='rosbridge_websocket',
        name='rosbridge_websocket_node',
        condition=IfCondition(use_foxglove)
     ) 

    ros_api_node = Node(
        package='rosapi',
        executable='rosapi_node',
        name='rosbridge_websocket_node',
        condition=IfCondition(use_foxglove)
     ) 
     

    map_launch_file = os.path.join(get_package_share_directory(package_name),'launch','map.launch.py')

    return LaunchDescription([
        gamepad_node,
        teleop_node,
        laser_filter,
        rosbridge_websocket_node,
        ros_api_node,
        IncludeLaunchDescription( map_launch_file),       # SLAM map generator
    ])
    