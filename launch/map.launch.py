import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    map = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('slam_toolbox'),'launch','online_async_launch.py')]),
                    launch_arguments={'params_file': './src/hb_bot/config/mapper_params_online_async.yaml'}.items()
            )


#<remap from="scan" to="base_scan" />

    return LaunchDescription([
        map
    ])
