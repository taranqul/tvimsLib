from decimal import Decimal
import math
import numpy as np
import scipy
def laplass(u_value: Decimal) -> Decimal:
    sqrt_2pi = Decimal(math.sqrt(2 * math.pi))
    exponent = Decimal(-u_value**2 / 2)
    return (Decimal(1) / sqrt_2pi) * exponent.exp()

def integralLaplass(u_value: Decimal) -> Decimal:
    result = Decimal(scipy.stats.norm.cdf(float(u_value))) - Decimal('0.5')

    return result
