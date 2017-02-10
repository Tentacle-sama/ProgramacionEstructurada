#Autor: Equipo #5
#29/enero/2017
#Entradas: se ingresa un número para determinar si es primo o no.
#salida: imprime si un número es primo o no.
#procedimiento:
variable=0
#entrada.
numero=int(input("Ingrese numero\n"))
for i in range(1,numero+1):
 if(numero % i==0):
  variable=variable+1
if(variable!=2):
    #salida.
 print("No es primo")
else:
    #salida.
 print("Si es primo")
