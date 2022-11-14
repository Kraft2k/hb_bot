## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `my_bot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).



// On bot run
ros2 launch hb_bot launch_robot.launch.py

// On host run
ros2 launch hb_bot gamepad.launch.py



sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers
sudo apt install ros-humble-xacro

colcon build --symlink-install 
colcon build --symlink-install --packages-select ros2_hoverboard_hardware

ros2 run teleop_twist_keyboard teleop_twist_keyboard -r /cmd_vel:=/diff_cont/cmd_vel_unstamped


pi
===
Enable camera
-------------

// Add ROS camera driver
sudo apt install libraspberrypi-bin v4l-utils ros-humble-v4l2-camera

// Add to video group
sudo usermod -aG video andrew

// Add ROS image transports
sudo apt install ros-humble-image-transport-plugins

// Check camera
vcgencmd get_camera
// Use to stream camera from pi - test
raspistill -k
// Check video for linux
v4l2-ctl --list-devices
  
//Run ROS camera standalone  
ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]" -p camera_fram_id:=camera_link_optical

// ROS image viewer
ros2 run rqt_image_view rqt_image_view

Lidar
=====
Build YLidar SDK
----------------
git clone https://github.com/YDLIDAR/YDLidar-SDK.git
cd YDLidar-SDK/
ls
mkdir build
cd build
cmake ..
make
sudo make install

Download ROS2 driver for YLidar
-------------------------------
git clone https://github.com/rekabuk/ydlidar_ros2_driver.git





