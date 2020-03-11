import unittest
import Libreria
import math
class Pruebaa(unittest.TestCase):
    
    def test_Canicas(self):
        X = [True, False, True]
        Matriz = [[True, True, False], [True, False, False], [True, False, True]]
        Click = 1
        cont = 1
        self.assertEqual(Libreria.Canicas(Matriz, X, Click, cont), [1, 1, 2])

        
    def test_RendijaProbabilistico(self):
        X = [1/3, 0, 2/3]
        Matriz = [[0, 1/3, 2/3], [1/6, 1/2, 1/3], [5/6, 1/6, 0]]
        Click = 1
        cont = 1
        self.assertEqual(Libreria.RendijaProbabilistico(Matriz, X, Click, cont), [0.4444444444444444, 0.2777777777777778, 0.2777777777777778])

        
    def test_DobleRendija(self):
        X = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]
        Matriz = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(1/math.sqrt(2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(1/math.sqrt(2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(0, 0), (-1/math.sqrt(6), 1/math.sqrt(6)), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                  [(0, 0), (-1/math.sqrt(6), -1/math.sqrt(6)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
                  [(0, 0), (1/math.sqrt(6), -1/math.sqrt(6)), (-1/math.sqrt(6), 1/math.sqrt(6)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
                  [(0, 0), (0, 0), (-1/math.sqrt(6), -1/math.sqrt(6)), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
                  [(0, 0), (0, 0), (1/math.sqrt(6), -1/math.sqrt(6)), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]
        cont = 1
        Click = 1
        self.assertEqual(Libreria.DobleRendija(Matriz, X, Click, cont), [[(0, 0)], [(0.7071067811865475, 0.0)], [(0.7071067811865475, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)], [(0.0, 0.0)]] )
        
if __name__ == "__main__":
    unittest.main()
