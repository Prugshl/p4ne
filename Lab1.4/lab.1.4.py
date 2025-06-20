import random
import ipaddress
from ipaddress import IPv4Network

from numpy.ma.core import append


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        network = random.randint(0x0B000000, 0xDF000000)
        prefix = random.randint(8, 24)
        ipaddress.IPv4Network.__init__ (self, (network, prefix), strict = False )
    def regular (self):
        return self.is_global
print(IPv4RandomNetwork())

iplist = []
for _ in range(50):
    subnet = IPv4RandomNetwork()  # Создаём экземпляр случайной подсети
    iplist.append(subnet)        # Добавляем в список
#print(iplist)  # Выводим список подсетей

def value_ip(net):
    return int(net.netmask) * 2**32 + int(net.network_address)

iplist.sort(key=value_ip)
print(iplist)