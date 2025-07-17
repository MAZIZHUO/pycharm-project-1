from decimal import Decimal, getcontext

def bbp_pi(digits):
    getcontext().prec = digits + 2
    pi = Decimal(0)
    for k in range(digits):
        term = (Decimal(1)/(16**k)) * (
            Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) -
            Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)
        )
        pi += term
    return pi

print(f"BBP公式（100位）：{bbp_pi(100)}")  # 输出前100位
