import json

class Router:
# Use python constructor to avoid the attribute mistakes
    def __init__(self, hostname, enable, motd, encryption, ip_add, username, password):
        self.hostname = hostname
        self.enable = enable
        self.ip_add = ip_add
        self.motd = motd
        self.encryption = encryption
        self.username = username
        self.password = password

    def router_configuation(self):
        print("Configuring the R1 Router to following settings\n")
        print(self.hostname)
        print(self.ip_add)
        print(self.motd)
        print(self.encryption)
        print(self.username)
        print(self.password)

if __name__ == '__main__':
    with open('R1.json') as f:
        data = json.load(f)

    r1 = Router(data['hostname'], data['enable'], data['motd'], data['encryption'], data['ip_address'], data['username'], data['password'])

    r1.router_configuation()