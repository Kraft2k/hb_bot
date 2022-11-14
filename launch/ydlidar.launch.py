import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    lidar_params_file = os.path.join(get_package_share_directory('hb_bot'),'config','gamepad.yaml')

    return LaunchDescription([

        Node(
            package='ydlidar_ros2_driver',
            executable='ydlidar_ros2_driver_node',
            output='screen',
            emulate_tty=True,
            parameters=[lidar_params_file],
            namespace='/'
         )
    ])
