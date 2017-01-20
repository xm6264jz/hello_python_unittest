import random

facts = ['For a right-angled triangle, the square of the longest side is equal to the squares of the two other sides',
'Scalene, isosceles, equilateral, and right-angle are types of triangle',
'Google Play, Delta Airlines, and CAT all have triangles in their logos',
'The Sierpinski Triangle is a fractal form, composed of an equilateral triangle recursively subdivded into smaller triangles']

def random_fact():
    return random.choice(facts)
