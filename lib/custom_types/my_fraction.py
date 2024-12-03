import decimal
class MyFraction:
    numerator: int
    denominator: int
    
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        num = self.numerator + other.numerator
        den = other.denominator
        return MyFraction(num, den)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def value(self) -> decimal.Decimal:
        return decimal.Decimal(float(self.numerator))/decimal.Decimal(float(self.denominator))