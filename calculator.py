class Calculator:

    # @staticmethod
    def addition(self, a, b):
        return a + b

     
    # @staticmethod
    def subtraction(self, a, b):
        return a - b

    # @staticmethod
    def multiplication(self, a, b):
        return a * b

    # @staticmethod
    def division(self, a, b):
        if b == 0:
            raise ValueError("B can't be zero!!!!")
        return a / b
    