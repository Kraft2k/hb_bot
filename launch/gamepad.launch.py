import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    
    gamepad_params_file = os.path.join(get_package_share_directory('hb_bot'),'config','gamepad.yaml')

    gamepad_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[gamepad_params_file]
            )
    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_node',
        parameters=[gamepad_params_file],
        remappings=[('/cmd_vel','/diff_cont/cmd_vel_unstamped')]
            )

    return LaunchDescription([
        gamepad_node,
        teleop_node
    ])