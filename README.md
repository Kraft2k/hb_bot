
<p>This is a hoverboard robot inspired by the work of https://github.com/EFeru/hoverboard-firmware-hack-FOC and his modifications to the hoverboard controller.<br>
Also to Norbert for his work https://homofaciens.de/technics-robots-R15-construction_en.htm and help with the CAD.<br>
And finally the great videos by Josh Newans https://www.youtube.com/c/ArticulatedRobotics which got me from zero to a working ROS2 robot in about 5wks!<br></p>

Thank-you to all you guys!



Useful Notes
============
More for my own memory than anything else!

ROS2 Install
>https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

>sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers
>sudo apt install ros-humble-xacro

>colcon build --symlink-install 
>colcon build --symlink-install --packages-select ros2_hoverboard_hardware


Normal run
----------
On bot run
>ros2 launch hb_bot launch_robot.launch.py

On host run - set use_local_gamepad false when running with "ros-ui-react"
>ros2 launch hb_bot gamepad.launch.py use_local_gamepad:=true



Run Teleop twist stand alone
>ros2 run teleop_twist_keyboard teleop_twist_keyboard -r /cmd_vel:=/diff_cont/cmd_vel_unstamped


PI camera
=========

Add ROS camera driver
>sudo apt install libraspberrypi-bin v4l-utils ros-humble-v4l2-camera

Add to video group
>sudo usermod -aG video andrew

Add ROS image transports
>sudo apt install ros-humble-image-transport-plugins

Check camera
>vt_cgencmd gecamera

Use to stream camera from pi - test
>raspistill -k

Check video for linux
>v4l2-ctl --list-devices
  
Run ROS camera standalone  
>ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]" -p camera_frame_id:=camera_link_optical

ROS image viewer
>ros2 run rqt_image_view rqt_image_view

Lidar
=====
Build YLidar SDK
----------------

>git clone https://github.com/YDLIDAR/YDLidar-SDK.git<br>
>cd YDLidar-SDK/<br>
>mkdir build<br>
>cd build<br>
>cmake ..<br>
>make<br>
>sudo make install<br>

Download ROS2 driver for YLidar
-------------------------------
>git clone https://github.com/rekabuk/ydlidar_ros2_driver.git

laser filters
-------------
>sudo apt-get install ros-humble-laser-filters

FoxGlove
========
>sudo apt install ros-humble-rosbridge-suite

run ROS2 bridge
>ros2 run rosbridge_server rosbridge_websocket

Run ROS2 bridge with debug and rosapi
>ros2 run rosbridge_server rosbridge_websocket DEBUG=ros2-web-bridge* node bin/rosbridge.js
>ros2 run rosapi rosapi_node

RPi
===

Monitor WiFi strength
>watch -n1 iwconfig

List available WiFi
>nmcli dev wifi
or
>sudo iwlist wlp1s0 scan | grep ESSID

Driver for RealTek 8188FU USB WiFi dongle
https://github.com/kelebek333/rtl8188fu


Tablet Teleop ros-ui-react
==========================
RPi
>ros2 run web_video_server web_video_server
>ros2 launch hb_bot launch_robot.launch.py

Dev
Disable gamepad_node in gamepad.launch.py 
>ros2 launch hb_bot gamepad.launch.py use_local_gamepad:=false
>ros2 run rosbridge_server rosbridge_websocket rosbridge_socket rosbridge_socket.py
Run web-server
>cd ws_dev/src/ros_ui-react/example
>npm start


SLAM
====

>sudo apt install ros-humble-slam-toolbox

>ros2 launch slam_toolbox online_async_launch.py params_file:=./src/hb_bot/config/mapper_params_online_async.yaml 
