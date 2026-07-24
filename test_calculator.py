import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        """ This method instantiate objects from Calculator class """
        self.calc = Calculator()
        


    def test_addition(self) -> None:
        # Mahyar
        pass

    def test_subtraction(self) -> None:
        # Roozbeh
        self.assertEqual(self.calc.subtraction(4,1), 3)
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
        