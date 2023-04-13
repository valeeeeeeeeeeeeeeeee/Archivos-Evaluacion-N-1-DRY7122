# ingreso de dirección IP octeto por octeto
octeto1 = input("ingresa el primer octeto: ")
octeto2 = input("ingresa el segundo octeto: ")
octeto3 = input("ingresa el tercer octeto: ")
octeto4 = input("ingresa el cuarto octeto: ")

# Union de dos octetos para formar la ip
direccion_ip = octeto1 + "." + octeto2 + "." + octeto3 + "." + octeto4

# Determinar si es una IP privada o publica
if direccion_ip.startswith("10.") or direccion_ip.startswith("172.16.") or dire>
	tipo_ip = "privada"
else:
	tipo_ip = "pública"
# Mostrar la dirección IP y el tipo en pantalla
print("La dirección IP es: " + direccion_ip)
print("Siendo una dirección IP: " + tipo_ip)

