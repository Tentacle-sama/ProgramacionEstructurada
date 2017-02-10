#Autor: Equipo #5
#29/enero/2017
#Entradas: se pide un número para descomponer en factores primos
#salida:  se imprimen todos los factores primos del mismo.
#procedimiento:
dos=int(2)
#entrada.
numero = int(input("Favor de ingresar el numero a calcular factores primos: "))
while(numero != 1):
  if(numero%dos==0):
    #salida.
       print(str(dos)," ")
       numero = numero / dos
  else:
       dos = dos + 1
