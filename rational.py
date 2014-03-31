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
        
        g = gcd(numer, denom)
        self.numer = numer//gcd(numer, denom)
        self.denom = denom//gcd(numer, denom)
    
    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)
    
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
        if isinstance(other, Rational):
            return Rational(self.numer*other.denom + other.numer*self.denom, self.denom*other.denom)
        if isinstance(other, int):
            return Rational(self.numer + other*self.denom, self.denom)
        return Rational(self.numer*other.denom + other.numer*self.denom, self.denom*other.denom) 
    
    def __iadd__(self, other):
        self = self.__add__(other)
        return self
    
    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numer*other.numer, self.denom*other.denom)
        if isinstance(other, int):
            return Rational(self.numer*other, self.denom)
        return Rational(self.numer*other.numer, self.denom*other.denom)
    
    def __imul__(self, other):
        self = self.__mul__(other)
        return self
    
    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numer*other.denom - other.numer*self.denom, self.denom*other.denom)
        if isinstance(other, int):
            return Rational(self.numer - other*self.denom, self.denom)
        return Rational(self.numer*other.denom - other.numer*self.denom, self.denom*other.denom)
    
    def __isub__(self, other):
        self = self.__sub__(other)
        return self
    
    def __floordiv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numer*other.denom, self.denom*other.numer)
        if isinstance(other, int):
            return Rational(self.numer, self.denom*other)
        return Rational(self.numer*other.denom, self.denom*other.numer)        

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numer*other.denom, self.denom*other.numer)
        if isinstance(other, int):
            return Rational(self.numer, self.denom*other)
        return Rational(self.numer*other.denom, self.denom*other.numer)
    
    def __ifloordiv__(self, other):
        self = self.__floordiv__(other)
        return self
    
    def __itruediv__(self, other):
        self = self.__truediv__(other)
        return self
    
    """
    def _richcmp(self, other, op):
        Helper for comparison operators, for internal use only.

        Implement comparison between a Rational instance `self`, and
        either another Rational instance or a float `other`.  If
        `other` is not a Rational instance or a float, return
        NotImplemented. `op` should be one of the six standard
        comparison operators.

        
        # convert other to a Rational instance where reasonable.
        if isinstance(other, numbers.Rational):
            return op(self._numerator * other.denominator,
                      self._denominator * other.numerator)
        if isinstance(other, float):
            if math.isnan(other) or math.isinf(other):
                return op(0.0, other)
            else:
                return op(self, self.from_float(other))
        else:
            return NotImplemented
    """
    
    

    def __lt__(self, other):
        """a < b"""
        if isinstance(other, Rational):
            return (self.numer*other.denom) < (self.denom*other.numer)
        return NotImplemented

    def __gt__(self, other):
        """a > b"""
        if isinstance(other, Rational):
            return (self.numer*other.denom) > (self.denom*other.numer)
        return NotImplemented

    def __le__(self, other):
        """a <= b"""
        if isinstance(other, Rational):
            return (self.numer*other.denom) <= (self.denom*other.numer)
        return NotImplemented

    def __ge__(self, other):
        """a >= b"""
        if isinstance(other, Rational):
            return (self.numer*other.denom) >= (self.denom*other.numer)
        return NotImplemented

    def __bool__(self):
        """a != 0"""
        return self.numer != 0

# Note that the numerator and the denominator of the rational numbers
# must be reduced to their smallest possible values. It may be helpful
# to implement a function that computes the Greatest Common Divisor of
# two numbers. You can make this a nested function in the constructor
# for the Rational class.

# if __name__ == "__main__":
#     print(Rational(4))