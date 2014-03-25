import rational

def main():
    first = Rational()
    print ('first:  ', first)
    second = Rational(4)
    print ('second:  ', second)
    third = Rational(25,10)
    print ("third:  0/1".format(third.numerator(), third.denominator())

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