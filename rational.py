from fractions import Fraction

class Rational(Fraction):
    """
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
        print("******CALLING OVERLOAD*******")
        return "{}/{}".format(self.numerator, self.denominator)
    
    """
    def numerator(self):
        # print("in numerator\n")
        return self.numer
    
    def denominator(self):
        # print("in denominator\n")
        return self.denom
    
    def __add__(self, other):
        # if isinstance(other, str):
        #     print("Triggered isinstance str catch")
        #     numer, denom = [eval(x) for x in other.split('/')]
        #     return self.__class__(self.numer+numer, self.denom+denom)
        if isinstance(other, int):
            
        return Rational(self.numer+other.numer, self.denom+other.denom)
    
    def __iadd__(self, other):
        self = self.__add__(other)
        return self
    
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