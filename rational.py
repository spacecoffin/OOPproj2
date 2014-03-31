from fractions import Fraction

class Rational(Fraction):
    def __init__(self, numer=0, denom=1):
        # print("in the ctor\n")
            
        def gcd(numer, denom):
            # print("in gcd\n")
            if numer == denom:
                return denom
            elif numer%denom == 0:
                return denom
            return gcd(denom, numer%denom)
        
        self.numer = numer//gcd(numer, denom)
        self.denom = denom//gcd(numer, denom)
    
    """
    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)
    
    def numerator(self):
        # print("in numerator\n")
        return self.numer
    
    def denominator(self):
        # print("in denominator\n")
        return self.denom
    
    def __add__(self):
        pass
    
    def __iadd__(self):
        pass
    
    def __mul__(self):
        pass
    
    def __imul__(self):
        pass
    
    def __sub__(self):
        pass
    
    def __isub__(self):
        pass
    """

# Note that the numerator and the denominator of the rational numbers
# must be reduced to their smallest possible values. It may be helpful
# to implement a function that computes the Greatest Common Divisor of
# two numbers. You can make this a nested function in the constructor
# for the Rational class.

# if __name__ == "__main__":
#     print(Rational(4))