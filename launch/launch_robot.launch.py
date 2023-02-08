import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, RegisterEventHandler, TimerAction
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.event_handlers import OnProcessStart
from launch.substitutions import LaunchConfiguration


from launch_ros.actions import Node


def generate_launch_description():
    #Set to ture to launch web server for Josh Newans ros_ui usage
    use_web_server_val = LaunchConfiguration('use_camera_web_server', default='false')

    package_name = 'hb_bot'

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py')]),
                    launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
            )

    robot_description = Command(['ros2 param get --hide-type /robot_state_publisher robot_description'])

    controller_params_file = os.path.join(get_package_share_directory(package_name),'config','my_controllers.yaml')


    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[{'robot_description': robot_description},  controller_params_file]
            )

    delayed_controller_manager = TimerAction(period=3.0, actions=[controller_manager])
 
    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )

    delayed_diff_drive_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[diff_drive_spawner],
        )
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    delayed_joint_broad_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[joint_broad_spawner],
        )
    )

    # Used to drive relays to control Motor driver
    hb_control = Node(
        package='hb_ctrl',
        executable='hb_node'
    )


    camera_launch_file = os.path.join(get_package_share_directory(package_name),'launch','camera_robot.launch.py')

    ydlidar_launch_file = os.path.join(get_package_share_directory(package_name),'launch','ydlidar.launch.py')

    map_launch_file = os.path.join(get_package_share_directory(package_name),'launch','map.launch.py')

    # Launch them all!
    return LaunchDescription([
        rsp,
        hb_control,
        delayed_controller_manager,
        delayed_diff_drive_spawner,
        delayed_joint_broad_spawner,
        IncludeLaunchDescription( 
                PythonLaunchDescriptionSource(camera_launch_file), 
                launch_arguments={'use_camera_web_server':use_web_server_val}.items() ),
        IncludeLaunchDescription( ydlidar_launch_file),
        IncludeLaunchDescription( map_launch_file),       # SLAM map generator
        
   ])


