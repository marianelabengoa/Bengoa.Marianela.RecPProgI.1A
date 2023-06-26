
def reemplazarCaracteres(cadena:str, caracter1:str, caracter2:str)->str:
    contador = 0
    cadena_reemplazada = ""
    for caracter in cadena:
        if caracter == caracter1:
            cadena_reemplazada += caracter2
            contador += 1
        else:
            cadena_reemplazada += caracter
    return cadena_reemplazada, contador


cadena=input("ingrese la cadena: ")
caracter1=input("ingrese el caracter a reemplazar: ")
caracter2=input("ingrese el caracter que reemplaza al primero: ")

print(reemplazarCaracteres(cadena, caracter1, caracter2))