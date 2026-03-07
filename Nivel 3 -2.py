def mayor_de_tres_numeros(num1, num2, num3):
  mayor = num1
  if num2 > mayor:
    mayor = num2
  if num3 > mayor:
    mayor = num3
  return mayor
print(mayor_de_tres_numeros(11, 20, 5))
