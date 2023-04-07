import unittest
import calc

class TestCalc(unittest.TestCase):

    """def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 14)
    #OR below we can call directly and we can do more assert call with possible scenario
    """
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
        #here it is one test test_add with many scenario
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)
        #here it is one test test_add with many scenario
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)
        #here it is one test test_add with many scenario
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)

        #self.assertRaises(ValueError, calc.divide, 10, 2)
        #OR we can use context manager way
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        
    
'''#Pass test :only add_test result
python -m unittest test_calc.py
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

#Failed test: only add_test result
 python -m unittest test_calc.py
F
======================================================================
FAIL: test_add (test_calc.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\\Python-Practice\\unit_test\\test_calc.py", line 8, in test_add
    self.assertEqual(result, 14)
AssertionError: 15 != 14

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
'''

'''Above way to run is without adding main if we add main then no need to do -m unittest
    and we can directly call python test_calc.py 
'''

"""PS D:\\Python-Practice\\unit_test> python test_calc.py
....  #this 4 dots means all passed if any fail that it will be F on that place of dot
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK"""



if __name__ =='__main__':
    unittest.main()