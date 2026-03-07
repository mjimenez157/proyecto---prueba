def multiplicar_lista(lista, numero):
  resultado = [x * numero for x in lista]
  return resultado
print(multiplicar_lista([4, 5, 6], 7))
