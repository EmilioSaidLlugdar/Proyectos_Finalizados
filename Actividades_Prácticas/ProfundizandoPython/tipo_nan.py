import math
from decimal import Decimal

a = float('NaN') #not a number tipo de dato numerico indefinido
print(f'a: {a}')
print(f'Es NaN?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN?: {math.isnan(a)}')