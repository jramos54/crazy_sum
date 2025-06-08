import unittest
from crazy_sum import crazy_sum, convert_letter_to_number

class  TestCrazySum(unittest.TestCase):
    
    def test_posicion_letras(self):
        self.assertEqual(convert_letter_to_number('A'),1)
    
    def test_sum_without_params(self):
        #No hay marametros, el rultado es siempre 1
        self.assertEqual(crazy_sum(),1)
        
    def test_sum_only_one_param(self):
        # Solo un parametro, el resultado es sumarse a si mismo y respetar las reglas de pares e impares
        self.assertEqual(crazy_sum(1),-2) # 1 + 1 = 2 * -1 => -2
        self.assertEqual(crazy_sum(2),5) # 2 + 2 = 4 + 1 => 5
        self.assertEqual(crazy_sum(-2),-3) # -2 + -2 = -4 + 1 => -3
        self.assertEqual(crazy_sum('A'),"-2ZY") # A:1 --> 1 + 1 = 2 * -1 => -2 A:Z, B:Y
        self.assertEqual(crazy_sum('D'),"9ZXR") # D:4 --> 4 + 4 = 8 + 1 => 9 A:Z, C:X, I:R
    
    def test_sum_two_int_param(self):
        # Dos parametros siendo solo numeros y respetar las reglas de pares e impares
        self.assertEqual(crazy_sum(1, 1), -2) # 1 + 1 = 2 * -1 => -2
        self.assertEqual(crazy_sum(1, 2), 2) # 1 + 2 = 3 - 1 => 2
        self.assertEqual(crazy_sum(2, 2), 5) # 2 + 2 = 4 + 1 => 5
        self.assertEqual(crazy_sum(-2, 1), -2) # -2 + 1 = -1 - 1 => -2
        
    def test_sum_letter_and_int(self):
        # Dos parametros siendo numero, letra y respetar las reglas de pares e impares
        self.assertEqual(crazy_sum(1, "A"), "-2ZY") # A:1 1 + 1 = 2 * -1 => -2  A:Z, B:Y
        self.assertEqual(crazy_sum(2, "A"), "2ZY") # A:1 2 + 1 = 3 - 1 => 2  A:Z, B:Y
        self.assertEqual(crazy_sum(2, "D"), "7ZT") # D:4 2 + 4 = 6 + 1 => 7  A:Z, G:T
        self.assertEqual(crazy_sum(-2, "B"), "1Z") # B:2 -2 + 2 = 0 + 1 => 1  A:Z
        self.assertEqual(crazy_sum(-5, "C"), "2ZY") # C:3 -5 + 3 = -2 * -1 => 2  A:Z, B:Y
        self.assertEqual(crazy_sum(-3, "F"), "4ZYW") # F:6 -3 + 6 = 3 + 1 => 4  A:Z, B:Y, D:W
        self.assertEqual(crazy_sum(-3, "B"), 0) # B:2 -3 + 2 = -1 + 1 => 0  A:Z
        
        
if __name__=="__main__":
    unittest.main()