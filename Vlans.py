num_vlan = int(input("Ingrese el número de VLAN: "))

if 1<= num_vlan <= 1005:
    print("La Vlan", num_vlan, "está en el rango normal.")
elif 1006 <= num_vlan <= 4094:
    print("La Vlan", num_vlan, "está en el rango extendido.")
else:
    print("La Vlan", num_vlan, "no es válida.")