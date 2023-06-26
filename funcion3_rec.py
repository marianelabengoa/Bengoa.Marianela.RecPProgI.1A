
def ordenarCaracteres(cadena:str)->str:
    tam = len(cadena)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if (cadena[i] > cadena[j]):
                aux = cadena[i]
                cadena[i] = cadena[j]
                cadena[j] = aux
    
print(ordenarCaracteres("algoritmo"))