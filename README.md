
This is a hoverboard robot inspired by the work of https://github.com/EFeru/hoverboard-firmware-hack-FOC and his modifications to the hoverboard controller.
Also to Norbert for his work https://homofaciens.de/technics-robots-R15-construction_en.htm and help with the CAD
And finally the great videos by Josh Newans https://www.youtube.com/c/ArticulatedRobotics which got me from zero to a working ROS2 robot in about 5wks!

Thank-you to all you guys!



Useful Notes
============
More for my own memory than anything else!


sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers
sudo apt install ros-humble-xacro

colcon build --symlink-install 
colcon build --symlink-install --packages-select ros2_hoverboard_hardware


On bot run
>ros2 launch hb_bot launch_robot.launch.py

On host run
>ros2 launch hb_bot gamepad.launch.py

Run Teleop twist stand alone
>ros2 run teleop_twist_keyboard teleop_twist_keyboard -r /cmd_vel:=/diff_cont/cmd_vel_unstamped


PI camera
=========

// Add ROS camera driver
sudo apt install libraspberrypi-bin v4l-utils ros-humble-v4l2-camera

// Add to video group
sudo usermod -aG video andrew

// Add ROS image transports
sudo apt install ros-humble-image-transport-plugins

Check camera
>vcgencmd get_camera

Use to stream camera from pi - test
>raspistill -k

Check video for linux
>v4l2-ctl --list-devices
  
Run ROS camera standalone  
>ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]" -p camera_fram_id:=camera_link_optical

ROS image viewer
>ros2 run rqt_image_view rqt_image_view

Lidar
=====
Build YLidar SDK
----------------

>git clone https://github.com/YDLIDAR/YDLidar-SDK.git
>cd YDLidar-SDK/
>ls
>mkdir build
>cd build
>cmake ..
>make
>sudo make install

Download ROS2 driver for YLidar
-------------------------------
>git clone https://github.com/rekabuk/ydlidar_ros2_driver.git


FoxGlove
========
>sudo apt install ros-humble-rosbridge-suite

run ROS2 bridge
>ros2 run rosbridge_server rosbridge_websocket

Run ROS2 bridge with debug
>ros2 run rosbridge_server rosbridge_websocket DEBUG=ros2-web-bridge* node bin/rosbridge.js

>ros2 run rosapi rosapi_node





