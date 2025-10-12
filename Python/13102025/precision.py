import decimal
from decimal import Decimal

print(decimal.getcontext())
decimal.getcontext().prec = 28
b = Decimal(1) / Decimal(7)
print(b)

decimal.getcontext().prec = 6
c = Decimal(1) / Decimal(7)
print(c)

d = b*c
print(d)
