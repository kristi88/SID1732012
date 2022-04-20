from netmiko import Netmiko
import re

net_connect = Netmiko(
   "192.168.56.106",
   username="cisco",
   password="cisco123!",
   device_type="cisco_ios",
)

#print(net_connect.find_prompt())
command = "show ip route connected"
output = net_connect.send_command(command)
net_connect.disconnect()

#output = ("Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP\n"
#"D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area \n" 
#"N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2 \n"
#"E1 - OSPF external type 1, E2 - OSPF external type 2 \n"
#"i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2 \n"
#"ia - IS-IS inter area, * - candidate default, U - per-user static route \n"
#"o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP \n"
#"a - application route \n"
#"+ - replicated route, % - next hop override, p - overrides from PfR \n"
#"Gateway of last resort is not set\n"
#"192.168.56.0/24 is variably subnetted, 2 subnets, 2 masks\n"
#"C        192.168.56.0/24 is directly connected, GigabitEthernet1\n"
#"C        192.168.56.106/32 is directly connected, GigabitEthernet1\n"
#"C        10.10.0.0/16 is directly connected, GigabitEthernet1")

nets = re.findall('C\s+[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\/[0-9]+', output)
lnets = []

for i in nets:
   x = i.replace('C', '')
   lnets.append(x.replace(' ', ''))

#print(lnets)

t_dict = {}
l_net_d = []

for i in lnets:
   x = i.split('/')
   t_dict["network"] = x[0]
   t_dict["mask"] = x[1]
   l_net_d.append(t_dict.copy())

#print(l_net_d)

def len2mask(len):
    """Convert a bit length to a dotted netmask (aka. CIDR to netmask)"""
    mask = ''
    if not isinstance(len, int) or len < 0 or len > 32:
        print("Illegal subnet length: %s (which is a %s)" % (str(len), type(len).__name__))
        return None
    
    for t in range(4):
        if len > 7:
            mask += '255.'
        else:
            dec = 255 - (2**(8 - len) - 1)
            mask += str(dec) + '.'
        len -= 8
        if len < 0:
            len = 0
    
    return mask[:-1]

for i in l_net_d:
   i["mask"] = len2mask(int(i["mask"]))

print(l_net_d)