def mayor_de_varios_numeros(*numeros):
  mayor = numeros[0]
  for num in numeros:
    if num > mayor:
      mayor = num
  return mayor
print(mayor_de_varios_numeros(7, 13, 15, 9, 5))
