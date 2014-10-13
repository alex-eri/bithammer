ARP_POISON = False
SSH_BAN = True

#keywords are {ip},{port},{mac}
BAN_RULE = [
    '/ip firewall filter add chain=forward action=drop comment=bithammer dst-address={ip} dst-port={port} protocol=tcp',
    '/ip firewall filter add chain=forward action=drop comment=bithammer dst-address={ip} dst-port={port} protocol=udp',
    ]

LOGIN = 'admin'
PASSWORD = 'secret'
#None if gateway is same with hosts gateway
GATEWAY = None

