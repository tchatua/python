from fabric.api import *
# fab -l
# fab system_info
#
# Execute command on local machine
def greeting(msg):
    # print "Good %" % msg
    print(f"good {msg}")
# Execute command on local machine
def system_info():
    print("Disk Space")
    local("df -h")
    print("RAM Size")
    local("free -m")
    print("System Update")
    local("uptime")
# Execute command on Remote machine
def remote_exec():
    print(f"Get System Info")
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")
    run("id") 
# sudo will escalate our privilege, run will not
sudo("yum install mariadb-server -y")
sudo("systemctl start mariadb")
sudo("systemctl enable mariadb")
# Setting up server using fabric