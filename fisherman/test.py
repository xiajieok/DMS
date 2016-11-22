import docker

client_ins = docker.Client(base_url='tcp://192.168.1.5:2375',version='1.20',timeout=10)
print(" Connect Successful !!!")