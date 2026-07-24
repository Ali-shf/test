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

    def division(a,b) -> None:
        #َArash
        if b == 0:
            raise ValueError("b cant be 0")
        return (a/b)
        

    def division_by_zero(self) -> None:
        # Zahra
        pass
        