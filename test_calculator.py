import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        """ This method instantiate objects from Calculator class """
        self.calc = Calculator()
        


    def test_addition(self) -> None:
        self.assertEqual(self.calc.addition(2,5), 7)
        pass

    def test_subtraction(self) -> None:
        # Roozbeh
        pass

    def test_multiplcation(self) -> None:
        # Ali
        pass

    def division(self) -> None:
        # Arash
        pass

    def division_by_zero(self) -> None:
        # Zahra
        pass
        