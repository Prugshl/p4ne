
from pysnmp.hlapi import *
import pysnmp
from pysnmp.hlapi import getCmd

result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.209", 161)),
                ContextData(),
                ObjectType(ObjectIdentity("SNMPv2-MIB", 'sysDescr', 0)))
#print(type(result))
ports = nextCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.209", 161)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode=False)
for x in result:
     for y in x[3]:
         print(y)

for x in ports:
     for y in x[3]:
         print(y)
