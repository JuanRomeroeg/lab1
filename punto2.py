import getpass
import telnetlib

HOST = "192.168.21.6"
user = input("Enter your username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Entrar al modo de configuración
tn.write(b"conf t\n")

# Configurar 4 VLAN con nombres de VLAN
tn.write(b"vlan 2\n")
tn.write(b"name Data_vlan_2\n")
tn.write(b"exit\n")
tn.write(b"vlan 3\n")
tn.write(b"name Data_vlan_3\n")
tn.write(b"exit\n")
tn.write(b"vlan 4\n")
tn.write(b"name Voice_vlan_4\n")
tn.write(b"exit\n")
tn.write(b"vlan 5\n")
tn.write(b"name Wireless_vlan_5\n")
tn.write(b"exit\n")

# Configurar ether 1/0 -- 1/3  como switchports de acceso y asignar VLAN 5 para APs inalámbricos
tn.write(b"interface ethernet 1/0 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 5\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface ethernet 1/1 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 5\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface ethernet 1/2 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 5\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface ethernet 1/3 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 5\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")

# Configurar ether 2/0-- 2/3  como switchports de acceso y asignar VLAN 2 para datos y VLAN 4 para voz
tn.write(b"interface ethernet 2/0 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 4\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface ethernet 2/1 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 4\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface ethernet 2/2 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 4\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")
tn.write(b"interface ethernet 2/3 \n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 4\n")
tn.write(b"no shut\n")
tn.write(b"exit\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))