class Rational:
    def __init__(self, numer=0, denom=1):
        print("in the ctor\n")
        self.numer = numer
        self.denom = denom
        
    @staticmethod
    def gcd(numer, denom):
        print("in gcd\n")
        if numer == denom:
            return denom
        elif numer%denom == 0:
            return denom
        return gcd(denom, numer%denom)
    
    def __str__(self):
        # print("in __str__\n")
        return "{}/{}".format(self.numer, self.denom)
    
    def numerator(self):
        print("in numerator\n")
        return self.numer/gcd(self.numer, self.denom)
    
    def denominator(self):
        print("in denominator\n")
        return self.denom/gcd(self.numer, self.denom)

# Note that the numerator and the denominator of the rational numbers
# must be reduced to their smallest possible values. It may be helpful
# to implement a function that computes the Greatest Common Divisor of
# two numbers. You can make this a nested function in the constructor
# for the Rational class.

# if __name__ == "__main__":
#     print(Rational(4))