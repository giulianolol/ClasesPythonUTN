#Esta función recibe 2 valores (int) y retrona la suma de estos 2 valores
def calcular_suma(primer_operando, segundo_operando):
    resultado = primer_operando + segundo_operando
    return resultado

#Esta función recibe 2 valores (int) y retrona la resta de estos 2 valores
def calcular_resta(primer_operando, segundo_operando):
    return primer_operando - segundo_operando

#Esta función recibe 2 valores (int) y retrona la division de estos 2 valores y avisa si se manda un cero
def calcular_division(primer_operando, segundo_operando):
    if segundo_operando == 0:
        return "No se puede dividir por cero"
    else: return primer_operando / segundo_operando
    
#Esta función recibe 2 valores (int) y retrona la multiplicación de estos 2 valores
def calcular_multiplicacion(primer_operando, segundo_operando):
    return primer_operando * segundo_operando

#Esta función recibe 2 valores (int) y retrona la potencia de el primer valor
def calcular_potencia(primer_operando, segundo_operando):
    
    for x in range(segundo_operando):
    
        if x == 0:
            
            resultado = primer_operando * primer_operando
        
        else:
            
            resultado = (resultado * segundo_operando)
    
    return resultado

#Esta función recibe 2 valores (int) y retrona el resto entre estos 2 valores
def calcular_resto(primer_operando, segundo_operando):
    if segundo_operando == 0:
        return "No se puede dividir por cero"
    return primer_operando % segundo_operando

#Esta función recibe el valor A (int) y retorna su factorial
def calcular_factorial_A(primer_operando):
        
    if primer_operando == 0:
        
        return 1
    
    else:
        
        return primer_operando * calcular_factorial_A(primer_operando-1)

#Esta función recibe el valor B (int) y retorna su factorial
def calcular_factorial_B(segundo_operando):
        
    if segundo_operando == 0:
        
        return 1
    
    else:
        
        return segundo_operando * calcular_factorial_A(segundo_operando-1)