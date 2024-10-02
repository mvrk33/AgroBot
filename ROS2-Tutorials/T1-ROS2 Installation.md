# ROS 2 Jazzy Installation on Ubuntu Noble 24

## Prerequisites
- Ubuntu 24.04

### 1. Update Ubuntu Package List

First, update your package list to ensure all existing packages are up to date.

```bash
sudo apt update && sudo apt upgrade -y
```
### 2. System setup
#### Set locale
Make sure you have a locale which supports UTF-8. If you are in a minimal environment (such as a docker container), the locale may be something minimal like POSIX. We test with the following settings. However, it should be fine if you’re using a different UTF-8 supported locale.

```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

### 3. Enable required repositories
You will need to add the ROS 2 apt repository to your system.

First ensure that the Ubuntu Universe repository is enabled.
```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```
Now add the ROS 2 GPG key with apt.

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Then add the repository to your sources list.
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### 4. Install ROS 2
Update your apt repository caches after setting up the repositories.

ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.


```bash
sudo apt update && sudo apt upgrade -y
```

#### 4.1 Desktop Install 
(Recommended for Laptops): ROS, RViz, demos, tutorials.

```bash
sudo apt install ros-jazzy-desktop
```

#### 4.2 ROS-Base Install 
(Bare Bones for Raspberry Pi or SBC's): Communication libraries, message packages, command line tools. No GUI tools.
```bash
sudo apt install ros-jazzy-ros-base
```

### 5. Setup environment
You can make the setup process immutable by using the following configuration to source the ROS 2 environment automatically each time you open a new shell:
```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```
Reload the shell to apply the changes:

```bash
source ~/.bashrc
```

### 6. Uninstall
If you need to uninstall ROS 2 or switch to a source-based install once you have already installed from binaries, run the following command:
```bash
sudo apt remove ~nros-jazzy-* && sudo apt autoremove
```

