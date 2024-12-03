import decimal
class MyIntervals:
    right: int
    left: int
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left}-{self.right}"
    
    def calculate_mean(self) -> decimal.Decimal:
        return decimal.Decimal((self.left + self.right) / 2)
    
    def calculate_diff(self) -> decimal.Decimal:
        return  decimal.Decimal(float(self.right - self.left))