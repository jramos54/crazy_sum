# deberian tener una responsabilidad unica
# Debe ser el manager de todas los requerimientos

import string

def sum_pares(a,b):
    return a+b+1

def sum_dobuble_b(a,b):
    return a+b+b+2

def sum_impares(a,b):
    return (a+b)*-1

def sum_mixtos(a,b):
    pass

def type_number(a):
    """Determinar si es par o impar
    return 
    True si es par
    False si es impar
    """
    if a%2==0:
        return True
    else:
        return False

def convert_letter_to_number(letra):
    letras=string.ascii_lowercase
    return letras.index(letra.lower())+1
    

def crazy_sum(a=None):
    
    if not a:
        return 1
    
    if type_number(a):
        return sum_pares(a,a)
    else:
        return sum_impares(a,a)
    
