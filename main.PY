import os
#1
print("Ejercicio 1")
total=0
for n in range(1,11):
 c=n**2
 total = total+c
 print('Número: ',n,' Cuadrado: ',c)
print("El total de los cuadrados de los primeros 10 números naturales es:",total)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#2
print("Ejercicio 2")
colores=["azul","verde","rojo","blanco","negro"]
for i in colores:
 print(i)
  # print(i, "", end="") para imprimir uno al lado del otro
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
 #3
print("Ejercicio 3")
numeros=[5,3,8,7,9,10,2,4,1,17]
for u in numeros:
  if u >4:
   print(u,"es mayor a 4")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#4
print("Ejercicio 4")
alumnos = [['Juan', 5], ['Pepe', 6.8], ['Alfredo', 4.5], ['Brenda', 10], ['Candela', 8], ['Francisco', 7.5], ['Jerónimo', 0], ['Fredi', 8.7], ['Tiziano', 7.8], ['Macarena', 8.5], ['Pablo', 5.5], ['Fabricio', 3.5], ['Lucas', 6.5], ['Lucio', 4.5], ['Uma', 7.5]]
for alumno in ( alumnos):
 if alumno[1]>7:
    print(alumno[0],"tiene una nota mayor de 7 que es:",alumno[1])
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#5
print("Ejercicio 5")
nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
menores=0
for numero in nums:
  if numero <15:
    menores=menores+1
print("El porcentaje menor a 15 fue:",(menores*100)/20,"%")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#6
print("Ejercicio 6")
total=0
for n in range(1,11):
 total = total+n
print("La sumatoria de los primeros 10 números naturales es:",total)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#7
print("Ejercicio 7")
numeross=[-88, 54, 54, -74, 44, 29, -36, -20, -79, 83, 47, -65, 38, -23, -67, -35, 60, 88, 8, -87]
for k in numeross:
  if k<0:
    print(k,"es negativo")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#8
print("Ejercicio 8")
for o in range(1,51):
  if o%2==0:
    print(o)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#9
print("Ejercicio 9")
total=0
for t in range(5):
  num=int(input(f"Ingrese el {t+1}° número: "))
  total=total+num
print("La sumatoria de todos los números es:",total)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#10
print("Ejercicio 10")
numbers =[-900, 137, 318, 349, 949, -140, -40, 898, -158, 74, 469, -428, -436, -492, 258, 524, -16, -135, 283, 655]
pos = 0
neg = 0
for y in numbers:
  if y >0:
    pos = pos+1
  else:
    neg=neg+1
print("Hay",pos,"números positivos y",neg,"números negativos")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#11
print("Ejercicio 11")
for q in range(10,101):
  if q%10==0:
    print(q)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#12
print("Ejercicio 12")
for r in range(10, 0, -1):
    print(r)
input("\033[1mPresione enter para salir\033[0m")
os.system('cls')