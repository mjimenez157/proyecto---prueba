def promedio(*numeros):
  total = sum(numeros)
  cantidad = len(numeros)
  return total / cantidad
print(promedio(2, 10, 14))
