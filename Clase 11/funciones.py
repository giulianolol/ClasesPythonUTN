def convertir_a_matriz(cadena):

    vocales = 'aeiou'

    conteo_vocales = [0] * len(vocales)

    for char in cadena.lower():
        if char in vocales:
            index = vocales.index(char)
            conteo_vocales[index] += 1

    matriz_vocales = [[vocal, conteo_vocales[i]] for i, vocal in enumerate(vocales)]
    
    return matriz_vocales

