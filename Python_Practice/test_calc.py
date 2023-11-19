import unittest
import UnitTest #importing from another module in the directory

class TestCalc(unittest.TestCase):
    #test methods have to start with test_
    def test_add(self):
        self.assertEqual(UnitTest.add(10,5), 15)
        self.assertEqual(UnitTest.add(-10,5), -5)
        self.assertEqual(UnitTest.add(-100,-5), -105)
        
    def test_subtract(self):
        self.assertEqual(UnitTest.subtract(10,5), 5)
        self.assertEqual(UnitTest.subtract(-10,5), -15)
        self.assertEqual(UnitTest.subtract(-100,-5), -95)
        
    def test_multiply(self):
        self.assertEqual(UnitTest.multiply(10,5), 50)
        self.assertEqual(UnitTest.multiply(-10,5), -50)
        self.assertEqual(UnitTest.multiply(-100,-5), 500)
        
    def test_divide(self):
        self.assertEqual(UnitTest.divide(10,5), 2)
        self.assertEqual(UnitTest.divide(-10,5), -2)
        self.assertEqual(UnitTest.divide(-100,-5), 20)
        
        self.assertRaises(ValueError, UnitTest.divide, 10, 0)
        # Could ue context managers to test for exceptions as well
        with self.assertRaises(ValueError):
            UnitTest.divide(10,0)
        
if __name__ == "__main__":
    unittest.main()
