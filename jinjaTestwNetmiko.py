from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")

interface_dict = {
    "name": "GigabitEthernet1",
    "description": " Server port",
    "ip": "192.168.56.106",
    "mask": "255.255.255.0"
}

commands = template.render(interface=interface_dict)
listofC = commands.split('\n')

net_connect = Netmiko(
   "192.168.56.106",
   username="cisco",
   password="cisco123!",
   device_type="cisco_ios",
)

print(net_connect.find_prompt())
output = net_connect.send_config_set(listofC)
net_connect.disconnect()
print(output)