def contador_vocales():
    cadena = input("Ingrese una frase: ")
    vocales = "aeiou"
    contador =0
    for letra in cadena:
        if letra in vocales:
            contador +=1
    return contador
resultado = contador_vocales()
print("Número de vocales: ", resultado)
