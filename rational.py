from fractions import Fraction

class Rational(Fraction):    
    def __init__(self, numer=0, denom=1):
        
        def gcd(numer, denom):
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
        return self.numer
    
    def denominator(self):
        return self.denom

    def __add__(self, other):
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

if __name__ == '__main__':
    from rational import Rational

    first = Rational()
    print ('first:  ', first)
    second = Rational(4)
    print ('second:  ', second)
    third = Rational(25,10)
    print ("third:  {0}/{1}".format(third.numerator(), third.denominator()))

    first += third
    print ('first:  ', first)
    third *= 8
    print ('third:  ', third)
    third /= first
    print ('third:  ', third)
    fourth = Rational(18,158)
    print ('fourth:  ', fourth)
    third -= fourth
    print ('third:  ', third)
    fourth = first + second
    print ('fourth:  ', fourth)
    
    if fourth == third:
        print ('The two rationals are the same')
    elif fourth > third:
       print ('fourth rational is greater than the third rational')
    else:
       print ('fourth rational is smaller than the third rational')