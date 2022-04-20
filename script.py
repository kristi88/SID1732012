from netmiko import Netmiko
import json

with open('R1.json') as f:
  data = json.load(f)


net_connect = Netmiko(
   data["ip_addr"],
   username=data["username"],
   password=data["password"],
   device_type=data["device_type"],
)

# Running the commands on the remote router.
command = "show ip route connected"
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)