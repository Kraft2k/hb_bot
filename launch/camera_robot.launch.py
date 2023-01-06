import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration 
from launch.conditions import IfCondition
from launch.actions import DeclareLaunchArgument

use_web_server = LaunchConfiguration ('use_camera_web_server', default=False)

def generate_launch_description():


    camera_server = Node(
        package='web_video_server',
        executable='web_video_server',
        output='screen',
        condition=IfCondition(use_web_server)
   )

    camera_node =  Node(
        package='v4l2_camera',
        executable='v4l2_camera_node',
        output='screen',
        parameters=[{
            'image_size': [640,480],
            'camera_frame_id': 'camera_link_optical'
             }]
    )

    return LaunchDescription([
	    camera_node,
	    camera_server
    ])
