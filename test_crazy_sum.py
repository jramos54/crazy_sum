import unittest
from crazy_sum import crazy_sum, convert_letter_to_number

class TestCrazySum(unittest.TestCase):
    
    def test_posicion_letras(self):
        self.assertEqual(convert_letter_to_number('A'),1)
    
    def test_sum_without_params(self):
        # No hay parametros el resultado es siempre 1
        self.assertEqual(crazy_sum(),1)
    
    def test_sum_only_one_param(self):
        # Solo un parametro el resultado es sumarse a si mismo y respetar las reglas de pares e impares
        self.assertEqual(crazy_sum(1),-2) #1+1=2  => -2
        self.assertEqual(crazy_sum(2),5) # 2 + 2 = 4 +1 => 5
        self.assertEqual(crazy_sum(-2),-3) # -2 + -2 = -4 +1 => -3
        self.assertEqual(crazy_sum('A'),"3ZY") # A:1 --> 1+1=-2=>-2 1:A:Z,2:b:Y
        self.assertEqual(crazy_sum('D'),'7ZT') #D:4 --> 4+4=8-1 =7 A:z,F:
        

if __name__=="__main__":
    unittest.main()