#Autor: Equipo #5
#29/enero/2017
#Entradas: se solicita la entrada de la "n" cantidad de números primos a sumar.
#salida: un vector que contenga la cantidad de numeros primos, y tambien imprime la suma.
#procedimiento:
n,contador = 4,2
#entrada
numero=int(input("Ingrese el numero de numeros primos que desea sumar\n"))
if(numero>2):
 cadena = "2-3"
 while contador < numero:
  i=2
  while i<=n:
   if(i==n):
    cadena= cadena+"-"+str(i)
    contador=contador+1
   else:
    if(n % i ==0):
     i=n
   i=i+1
  n=n+1
else:
 if(numero>0):
  if(numero==1):
   cadena="2"
  else:
   cadena="2-3"
 else:
     #salida
  print("ingrese un numero positivo")
lista = cadena.split("-")
lista = list(map(int, lista))
#salida
print ("Lista de los ",numero," primeros numeros primos\n",lista)
suma=0
for i in lista:
 suma = suma + i
 #salida
print("La suma de los primeros ",numero," numero primos es igual a: ",suma)
