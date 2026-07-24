import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        """ This method instantiate objects from Calculator class """
        Calculator()

    def test_addition(self) -> None:
        # Mahyar
        pass

    def test_subtraction(self) -> None:
        # Roozbeh
        pass

    def test_multiplcation(self) -> None:
        res = Calculator.multiplication(2, 3)
        self.assertEqual(res, 6)
        pass

    def division(self) -> None:
        # Arash
        pass

    def division_by_zero(self) -> None:
        # Khodam
        pass
