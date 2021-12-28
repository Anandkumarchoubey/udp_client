import socket

target_host = "localhost"
target_port = 80

#create a sockt object
clint = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Send some some data
clint.sendto(b"This is test data",(target_host,target_port))
#receive some data
data,addr = clint.recvfrom(4096)

print(data.decode)

clint.close()