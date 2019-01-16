#python script to change mac address of  linux system using subprocess Module

import subprocess
subprocess.call("ifconfig", shell = "true")
#subprocess.run("ifconfig", shell = "true")
subprocess.call("ifconfig wlan0 down", shell = "true")
# "down" is used to taking down the wlan0 interface
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell = "true")
subprocess.call("ifconfig wlan0 hw up", shell = "true")
#"up" is to start the interface again
#subprocess.call() is used to run terminal or shell commands

#this script only changes mac address of wlan0 to 00:11:22:33:44:66
