import psutil
import platform

print (psutil.cpu_percent())

mem = psutil.virtual_memory()
capacidade = round(mem.total/(1024*1024*1024), 2)
print("Capacidade total de MP:", capacidade, "GB")

print(platform.processor())
print(platform.node())
print(platform.platform())
print(platform.system())



disco = psutil.disk_usage('.')

print("Total:", disco.total, "B")
print("Em uso:", disco.used, "B")
print("Livre:", disco.free, "B")

print("Total:", round(disco.total/(1024*1024*1024), 2), "GB")
print("Em uso:", round(disco.used/(1024*1024*1024), 2), "GB")
print("Livre:", round(disco.free/(1024*1024*1024), 2), "GB")

print("Percentual de Disco Usado:", disco.percent)


dic_interfaces = psutil.net_if_addrs()
print(dic_interfaces['eth0'][1].address)

ssh-keygen -t rsa -b 4096 -C jean.oliveira@al.infnet.edu.br  
ssh-add ~/.ssh/id_rsa  