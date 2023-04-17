import ipaddress

# Se solicita la dirección de red y el prefijo al usuario
direccion_red = input("Ingrese la dirección de red: ")
prefijo = int(input("Ingrese el prefijo: "))

# Se crea el objeto de red a partir de la dirección de red y el prefijo
red = ipaddress.IPv4Network((direccion_red, prefijo), strict=False)

# Se muestran las IPs asignables a los host
for ip in red.hosts():
    print(ip)
