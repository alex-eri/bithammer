ARP_POISON = False
SSH_BAN = True

# keywords are {ip},{port},{mac}
# must check existance before insert!
# mikrotik sample
BAN_RULES = [
'''if ([:len [/ip firewall filter find protocol="tcp" dst-port="{port}" dst-address="{ip}"]] = 0) else={put "exist"} do={
/ip firewall filter add chain=forward action=drop comment=bithammer dst-address="{ip}" dst-port="{port}" protocol="tcp"
}''',
'''if ([:len [/ip firewall filter find protocol="udp" dst-port="{port}" dst-address="{ip}"]] = 0) else={put "exist"} do={
/ip firewall filter add chain=forward action=drop comment=bithammer dst-address="{ip}" dst-port="{port}" protocol="udp"
}''',
    ]

LOGIN = 'admin'
PASSWORD = 'secret'
#None if gateway is same with hosts gateway
GATEWAY = None

