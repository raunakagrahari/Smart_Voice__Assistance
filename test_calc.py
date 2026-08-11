import unittest
import main

class TestCalculator(unittest.TestCase):
    def setUp(self):
        main.clrbut()

    def test_clickbut(self):
        main.clickbut(5)
        self.assertEqual(main.operator, '5')
        main.clickbut('+')
        main.clickbut(3)
        self.assertEqual(main.operator, '5+3')

    def test_equlbut(self):
        main.operator = '10+20'
        main.equlbut()
        self.assertEqual(main.textin.get(), '30')

    def test_equlbut_error(self):
        main.operator = '10/0'
        main.equlbut()
        self.assertEqual(main.textin.get(), 'Error')

if __name__ == '__main__':
    unittest.main()
