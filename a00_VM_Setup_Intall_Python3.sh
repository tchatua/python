#!/bin/bash
# vim /etc/hostname
    # python
sudo -i 
hostnamectl set-hostname python
###########################
### Source installation ###
###########################
# Source: URL: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
# 1/*** Update and Refresh Repository Lists
apt update -y 
# 2/*** Install Supporting Software
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
# 3/*** Download the Latest Version of Python Source Code
cd /tmp/
wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
# 4/*** Extract Compressed Files
tar -xf Python-3.11.1.tgz
# 5/*** Test System and Optimize Python
cd Python-3.11.1
./configure --enable-optimizations
# 6/*** Install a Second Instance of Python (recommended)
make altinstall
# 7/*** (Option) Overwrite Default Python Installation 
make install
# 8/*** Verify Python Version
python3 --version