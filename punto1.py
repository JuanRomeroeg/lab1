import getpass
import telnetlib

# Dirección IP del host al que nos conectaremos
HOST = "192.168.21.4"

# Solicitar al usuario su nombre de usuario
user = input("Enter your username: ")

# Solicitar al usuario su contraseña de forma segura
password = getpass.getpass()

# Establecer la conexión Telnet
tn = telnetlib.Telnet(HOST)

# Esperar hasta que aparezca "Username:" en la salida
tn.read_until(b"Username: ")

# Enviar el nombre de usuario codificado en formato ASCII y agregar una nueva línea
tn.write(user.encode('ascii') + b"\n")

# Verificar si se ingresó una contraseña
if password:
    # Esperar hasta que aparezca "Password:" en la salida
    tn.read_until(b"Password: ")

    # Enviar la contraseña codificada en formato ASCII y agregar una nueva línea
    tn.write(password.encode('ascii') + b"\n")

# Envío de comandos para configurar el dispositivo
tn.write(b"enable\n")
tn.write(b"cisco123\n")
tn.write(b"conf t\n")
tn.write(b"int loopback 0\n")
tn.write(b"ip add 2.2.2.2 255.255.255.255\n")
tn.write(b"int loopback 1\n")
tn.write(b"ip add 4.4.4.4 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")


# Imprimir la salida de la sesión Telnet decodificada en formato ASCII
print(tn.read_all().decode('ascii'))
