from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
import docker

client_ins = docker.Client(base_url='tcp://192.168.1.5:2375', version='1.20', timeout=10)
print(" Connect Successful !!!")


def index(request):
    host_ip = client_ins.info()
    # print(host_ip)
    # for k in host_ip:
    #     print(k,host_ip[k])
    name_host = host_ip['Name']
    num_imgs = len(client_ins.images())
    # 镜像数
    os_host = host_ip['OperatingSystem']
    # 操作系统类型
    num_cpu = host_ip['NCPU']
    # 内存
    mem_host = host_ip['MemTotal']//1024//1024
    # 内存
    num_containers = host_ip['Containers']

    base_url = client_ins.base_url
    for i in dir(client_ins):
        print(i)
    print(client_ins)
    return render(request, 'node/host.html', {'num_imgs': num_imgs,
                                              'name_host': name_host,
                                              'os_host': os_host,
                                              'num_cpu':num_cpu,
                                              'mem_host': mem_host,
                                              'num_containers': num_containers,
                                              })
    # stats = client_ins.search('nginx')
    # for i in stats:
    #     print(i)
    # return HttpResponse('ok')
