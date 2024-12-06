from decimal import Decimal
import math
def laplass(u_value: Decimal) -> Decimal:
    sqrt_2pi = Decimal(math.sqrt(2 * math.pi))
    exponent = Decimal(-u_value**2 / 2)
    return (Decimal(1) / sqrt_2pi) * exponent.exp()
