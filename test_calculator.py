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
        pass

    def test_multiplcation(self) -> None:
        # Ali
        pass

    def division(self) -> None:
        #َArash
        self.assertEqual(self.calc.division(10, 2), 5.0)

        pass

    def division_by_zero(self) -> None:
        # Zahra
        pass
        