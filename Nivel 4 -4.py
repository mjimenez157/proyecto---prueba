def calcular_mediana(*numeros):
  lista = sorted(numeros)
  num = len(lista)
  mitad = num // 2
  if num % 2 != 0: # impar
    return lista[mitad]
  else: # par
     return (lista[mitad - 1] + lista [mitad]) / 2
print(calcular_mediana(9, 1, 5))
print(calcular_mediana(9, 1, 5, 3))
