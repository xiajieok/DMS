from django.db import models

# Create your models here.
class node(models.Model):
    id = models.IntegerField(primary_key=True) #自增
    name = models.CharField(max_length=32)  #主机名
    ip = models.IPAddressField(max_length=32)   #节点IP
    port = models.CharField(max_length=32)  #监听端口
    cpus = models.CharField(max_length=32)  #CPU个数
    mem = models.CharField(max_length=32)   #内存数
    state = models.CharField(max_length=32) #节点状态
    node_group = models.CharField(max_length=32)    #节点所在的组
    containers = models.CharField(max_length=32)    #容器数
    os_version = models.CharField(max_length=32)    #系统版本
    kernel_version = models.CharField(max_length=32)    #内核版本
    docker_version = models.CharField(max_length=32)    #docker 版本
class con_usage(models.Model):
    id = models.IntegerField(primary_key=True)
    con_id = models.CharField(max_length=64)
    node_ip = models.CharField(max_length=32)
    user_name = models.CharField(max_length=32)
    con_app = models.CharField(max_length=32)
    con_desc = models.CharField(max_length=32)
