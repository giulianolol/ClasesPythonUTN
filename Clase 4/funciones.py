def sumar_naturales(numero:int)->int:
    
    if numero == 0:
        
        resultado = 0
    
    else:
        
        resultado =  numero + sumar_naturales(numero-1)
        
    return resultado

def calcular_potencia(base:int, exponente: int)-> int:
    
    if exponente == 0:
        
        resultado = 1
    
    elif exponente > 0:
        
        resultado =  base * calcular_potencia(base, exponente - 1)
    
    else:
        
        resultado = 1 / calcular_potencia(base, - exponente)

    return resultado

def suma_digitos(numero:int) -> int:
    
    if numero < 10:
        
        resultado = numero
    
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        resultado = ultimo_digito + suma_digitos(resto_numero)
        
    return resultado

def calcular_fibonacci(n:int)->int:
    if n <= 0:
        resultado = "Numero invalido"
    elif n == 1:
        resutlado =  0
    elif n == 2:
        resultado = 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        resultado = b
        
    return resultado