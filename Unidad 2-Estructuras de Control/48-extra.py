#Autor: Equipo #5
#29/enero/2017
#Entradas: se ingresa el seldo de un trabajador y los años trabajados.
#salida: imprime el porcentaje al cual es acreditado pro sus años laborales y cuanto es su pago extra.
#procedimiento:
porcentaje_extra = 0
verificador = False
while verificador == False:
    #entrada.
 sueldo = float(input("Favor de escirbir el sueldo del trabajador\n"))
 #entrada
 años = float(input("Escriba el numero de años trabajados\n"))
 if sueldo > 0:
  if años > 0:
      if (años >= 1) and (años <=3):
          #salida
          print("Porcentaje extra 1%")
          porcentaje_extra = (sueldo)*(0.01)
          verificador = True
      else:
          if (años >= 4) and (años <=6):
              #salida
              print("Porcentaje extra 3%")
              porcentaje_extra = (sueldo)*(0.03)
              verificador = True
          else:
              if (años >=7) and (años <=9):
                  #salida
                  print("Porcentaje extra 5%")
                  porcentaje_extra = (sueldo)*(0.05)
                  verificador = True
              else:
                  #salida
                  print("Porcentaje extra 7%")
                  porcentaje_extra = (sueldo)*(0.07)
                  verificador = True
                 
  else:
      #salida
      print("Numero de años no es mayor a cero")
      verificador = False
 else:
     #salida
     print("Suelde no es mayor a cero")
     verificador = False
suma = sueldo + porcentaje_extra
print(suma)
