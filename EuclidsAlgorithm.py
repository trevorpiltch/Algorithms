# Chapter 1
def gcd(a: int, b: int) -> int:
    """Euclids algorithm to find the greatest common divisor of two numbers a and b"""
    r = a % b 
    while r != 0:
        a = b
        b = r
        
        r = a % b 

    return b

print(gcd(12, 7))