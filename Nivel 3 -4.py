def buscar_palabra(cadena, palabra):
  if palabra in cadena:
    return True
  else:
    return False
print(buscar_palabra("hola mundo", "mundo"))
print(buscar_palabra("hola mundo", "casa"))
