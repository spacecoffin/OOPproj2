from fractions import Fraction

def main():
    first = Fraction()
    print ('first:  ', first)
    second = Fraction(4)
    print ('second:  ', second)
    third = Fraction(25,10)
    # print ("third:  {0}/{1}".format(third.numerator(), third.denominator()))

    first += third
    print ('first:  ', first)
    third *= 8
    print ('third:  ', third)
    third /= first
    print ('third:  ', third)
    fourth = Fraction(18,158)
    print ('fourth:  ', fourth)
    third -= fourth
    print ('third:  ', third)
    fourth = first + second
    print ('fourth:  ', fourth)
    
    if fourth == third:
        print ('The two Fractions are the same')
    elif fourth > third:
       print ('fourth Fraction is greater than the third Fraction')
    else:
       print ('fourth Fraction is smaller than the third Fraction')

main()