import math
from lib.custom_types.my_intervals import MyIntervals as mi
inter: mi = mi(-math.inf, math.inf, quantize_val='1', delimeter='-')
print(inter)