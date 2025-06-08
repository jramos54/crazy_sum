# Las funciones deberian tener una responsabilidad única
# Debe de ser el manager de todos los requerimientos

import string
def sum_pares(a, b):
    return (a + b) + 1

def sum_impares(a, b):
    return (a + b) * -1

def sum_dobule_b(a,b):
    return (a + 2*b) + 2

def sum_mixtos(a,b):
    return (a + b) - 1

def type_number(a):
    """Determinar si es par o impar
    return True si es par
    False si es impar"""
    if not a % 2:
        return True
    else:
        return False
    
def convert_letter_to_number(letra):
    letras=string.ascii_lowercase
    number = letras.index(letra.lower())+1
    return number

def dividers(number):
    global selected_dividers
    global alphabet 
    selected_dividers = []
    dividers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for divider in dividers:
        if number%divider == 0:
            selected_dividers.append(divider)
    return selected_dividers

def inv_letters():
    global selected_letters
    selected_letters = []
    inv_alph = alphabet[::-1]
    for index in selected_dividers:
        selected_letters.append(inv_alph[index-1])
    return selected_letters

# def result_one_letter():
#     letra = convert_letter_to_number(a)
#     return letra + "".join(selected_letters)
    

def crazy_sum(a=None, b=None):
    if not a and not b:
        return 1
    elif a and not b:
        if type(a) == str and not b:
            a = convert_letter_to_number(a)
            if type_number(a):
                result = sum_pares(a,a)
                dividers(result)
                inv_letters()
                return str(result) + "".join(selected_letters)
            else:
                result = sum_impares(a,a)
                dividers(result)
                inv_letters()
                return str(result) + "".join(selected_letters)
        else:
            if type_number(a):
                return sum_pares(a,a)
            else:
                return sum_impares(a,a)
    else:
        if type_number(a) and type_number(b):
            return sum_pares(a,b)
        elif type_number(a) and type_number(b) == False:
            return sum_mixtos(a,b)
        elif type_number(b) and type_number(a) == False:
            return sum_mixtos(a,b)
        else:
            return sum_impares(a,b)
        
    
