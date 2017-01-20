import math

def area(base, height):
    '''
    Compute the area of a triangle with the given base and height.
    Raises a ValueError if base or height are negative.
    '''

    if base < 0 or height < 0:
        raise ValueError('Base and height must be postiive. \
        Was given base: {}, height {}'.format(base, height))

    area = base * height / 2
    return area


def is_right_angle(s1, s2, s3):
    ''' Use Pythagoras' Theorum to determine if a triangle is right-angled'''

    # A triangle is right-angled if a**2 + b**2 == c**c
    # where c is the longest side (** is the power operator, a**2 means 'a squared')

    sides = [s1, s2, s3]  # Sort the sides, longest side last
    sides.sort()

    a, b, c = tuple(sides)   # Turn into a tuple and unpack into a, b, c variables

    if a**2 + b**2 == c**2:    # Pythagoras for integers
        return True

    # Floating point math rounding, return True if the values are within 1x10-9 of each other.
    return math.isclose(a**2 + b**2, c**2)     # is isClose for floating-point comparisons
