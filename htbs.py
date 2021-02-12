#!/usr/bin/python3
import sys
from os import system as cmd

# Banner
print(" \n  ___ ________________________    _________ _________     _____    _______")
print(" /   |   \__    ___/\______   \  /   _____/ \_   ___ \   /  _  \   \      \  ")
print("/    ~    \|    |    |    |  _/  \_____  \  /    \  \/  /  /_\  \  /   |   \ ")
print("\    Y    /|    |    |    |   \  /        \ \     \____/    |    \/    |    \ ")
print(" \___|_  / |____|    |______  / /_______  /  \______  /\____|__  /\____|__  / ")
print("       \/                   \/          \/          \/         \/         \/ \n\n")

# checking arguments
if len(sys.argv)==2:
        # get IP
        ip = ('10.10.10.'+sys.argv[1]) # if you're a THM user change this
        # default nmap
        cmd('nmap '+ip+' -oA normalscan')
        # seperating opened ports
        cmd("cat normalscan.nmap | grep open | awk -F/ '{print $1}' ORS=',' | rev | cut -c 2- | rev > opened-ports.txt")
        # opening ports file
        f=open("opened-ports.txt", "r")
        ports = f.read()
        print("\nOPENED PORTS:")
        print(ports)
        # scanning only the opened ports
        cmd('nmap -sC -sV '+ip+' -p'+ports)
        # deleting extra files ( I used -oN flag but it took more time than -oA. So, I used -oA and deleting the extra stuffs here )
        cmd('rm opened-ports.txt normalscan.gnmap normalscan.xml normalscan.nmap')
# printing usage
else:
        sys.stderr.write("Usage: {0} <last digits of IP>\n\n".format(sys.argv[0]))
