#최대공약수 (GCD)
def finding_gcd(a, b):
    while (b != 0):
        res = b
        a, b = b, a % b
    return res