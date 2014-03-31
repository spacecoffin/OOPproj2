def gcd(numer, denom):
    print("in gcd\n")
    if numer == denom:
        return denom
    elif numer%denom == 0:
        return denom
    return gcd(denom, numer%denom)

def main():
    print(gcd(25, 10))
    
main()