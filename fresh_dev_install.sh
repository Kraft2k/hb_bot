
sudo apt install python3-colcon-common-extensions

# ROS2 Humble
sudo apt install software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update

sudo apt upgrade

sudo apt install ros-humble-desktop

#Do we need this
sudo apt install ros-dev-tools

#Do we need this or is it part of the desktop install?
sudo apt install ros-humble-xacro



# Setup our workspace
mkdir -p ~/ws_dev/src
cd ~/ws_dev
colcon build --symlink-install

git clone https://github.com/rekabuk/hb_bot.git

git clone https://github.com/rekabuk/hb_ctrl.git

git clone https://github.com/rekabuk/ros2-hoverboard-driver.git


# Install the Lidar SDK
cd ~
git clone https://github.com/rekabuk/ydlidar_ros2_driver.git
cd YDLidar-SDK/
mkdir build
cd build
cmake ..
make
sudo make install

# Install the Lidar ROS2 driver
cd ~/ws_dev/src
git clone https://github.com/rekabuk/ydlidar_ros2_driver.git

# ROS SLAM Toolbox
sudo apt install ros-humble-slam-toolbox

# ROS Laser filters - I think we can get rid of this
sudo apt install ros-humble-laser-filters

# ROS bridge
sudo apt install ros-humble-rosbridge-server

# ROS control
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers 

# Foxglove suppot ???
sudo apt install ros-humble-rosbridge-suite

