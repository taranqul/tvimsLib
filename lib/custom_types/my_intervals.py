from decimal import Decimal
class MyIntervals:
    right: Decimal
    left: Decimal
    def __init__(self, left: Decimal, right: Decimal):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{(Decimal(float(self.left))).quantize(Decimal("1.0000"))} - {(Decimal(float(self.right))).quantize(Decimal("1.0000"))}"
    
    def calculate_mean(self) -> Decimal:
        return (self.left + self.right) / Decimal(2)
    
    def calculate_diff(self) -> Decimal:
        return self.right - self.left