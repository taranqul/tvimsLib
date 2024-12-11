from decimal import Decimal
class MyIntervals:
    right: Decimal
    left: Decimal
    quantize_val: str
    delimeter: str
    def __init__(self, left: Decimal, right: Decimal, quantize_val: str, delimeter: str):
        self.delimeter = delimeter
        self.quantize_val = quantize_val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{(Decimal(float(self.left))).quantize(Decimal(self.quantize_val))} {self.delimeter} {(Decimal(float(self.right))).quantize(Decimal(self.quantize_val))}"
    
    def calculate_mean(self) -> Decimal:
        return (self.left + self.right) / Decimal(2)
    
    def calculate_diff(self) -> Decimal:
        return self.right - self.left