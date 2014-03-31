from fractions import Fraction
import numbers

class Rational(Fraction):
    __slots__ = ('_numerator', '_denominator')
    
    def __init__(cls, numerator=0, denominator=1):
        """Constructs a Rational.

        Takes a string like '3/2' or '1.5', another Rational instance, a
        numerator/denominator pair, or a float.

        Examples
        --------

        >>> Fraction(10, -8)
        Fraction(-5, 4)
        >>> Fraction(Fraction(1, 7), 5)
        Fraction(1, 35)
        >>> Fraction(Fraction(1, 7), Fraction(2, 3))
        Fraction(3, 14)
        >>> Fraction('314')
        Fraction(314, 1)
        >>> Fraction('-35/4')
        Fraction(-35, 4)
        >>> Fraction('3.1415') # conversion from numeric string
        Fraction(6283, 2000)
        >>> Fraction('-47e-2') # string may include a decimal exponent
        Fraction(-47, 100)
        >>> Fraction(1.47)  # direct construction from float (exact conversion)
        Fraction(6620291452234629, 4503599627370496)
        >>> Fraction(2.25)
        Fraction(9, 4)
        >>> Fraction(Decimal('1.47'))
        Fraction(147, 100)

        """
        self = super(Rational, cls).__init__

        if denominator is 1:
            if isinstance(numerator, numbers.Rational):
                self._numerator = numerator.numerator
                self._denominator = numerator.denominator
                return self

            elif isinstance(numerator, float):
                # Exact conversion from float
                value = Fraction.from_float(numerator)
                self._numerator = value._numerator
                self._denominator = value._denominator
                return self

            elif isinstance(numerator, Decimal):
                value = Fraction.from_decimal(numerator)
                self._numerator = value._numerator
                self._denominator = value._denominator
                return self

            elif isinstance(numerator, str):
                # Handle construction from strings.
                m = _RATIONAL_FORMAT.match(numerator)
                if m is None:
                    raise ValueError('Invalid literal for Fraction: %r' %
                                     numerator)
                numerator = int(m.group('num') or '0')
                denom = m.group('denom')
                if denom:
                    denominator = int(denom)
                else:
                    denominator = 1
                    decimal = m.group('decimal')
                    if decimal:
                        scale = 10**len(decimal)
                        numerator = numerator * scale + int(decimal)
                        denominator *= scale
                    exp = m.group('exp')
                    if exp:
                        exp = int(exp)
                        if exp >= 0:
                            numerator *= 10**exp
                        else:
                            denominator *= 10**-exp
                if m.group('sign') == '-':
                    numerator = -numerator

            else:
                raise TypeError("argument should be a string "
                                "or a Rational instance")

        elif (isinstance(numerator, numbers.Rational) and
            isinstance(denominator, numbers.Rational)):
            numerator, denominator = (
                numerator.numerator * denominator.denominator,
                denominator.numerator * numerator.denominator
                )
        else:
            raise TypeError("both arguments should be "
                            "Rational instances")

        if denominator == 0:
            raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
        g = gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g
        return self
    
    @property
    def numerator(a):
        return a._numerator

    @property
    def denominator(a):
        return a._denominator

    def __str__(self):
        """str(self)"""
        return '%s/%s' % (self._numerator, self._denominator)
    
    def __copy__(self):
        if type(self) == Rational:
            return self     # I'm immutable; therefore I am my own clone
        return self.__class__(self._numerator, self._denominator)
    
    def __deepcopy__(self, memo):
        if type(self) == Rational:
            return self     # My components are also immutable
        return self.__class__(self._numerator, self._denominator)