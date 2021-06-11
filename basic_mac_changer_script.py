#!/usr/bin/env python

# Basic MAC Address Changer
# Jose E. Rodriguez
# Nothing super impressive here. Just a simple script that uses the subprocess module to issue commands and change the MAC address.

import subprocess   

# "wlan0" should be changed to whatever interface you want the new MAC address to be associated with.
subprocess.call("ifconfig wlan0 down", shell=True) 

# change the MAC address to whatever you want
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
 
subprocess.call("ifconfig wlan0 up", shell=True)