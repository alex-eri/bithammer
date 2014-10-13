ARP_POISON = False
SSH_BAN = True
BAN_RULE = [
    '/ip firewall filter add chain=forward action=drop dst-address={ip} dst-port={port} protocol=tcp',
    '/ip firewall filter add chain=forward action=drop dst-address={ip} dst-port={port} protocol=udp',
    ]

LOGIN = 'admin'
PASSWORD = 'secret'
