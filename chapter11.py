import math

def roots(a, b, c):
    """ return a list of solutions of ax^2 + bx + c = 0.
        if there are no roots, the list will be empty. Otherwise,
        the list will contain 1 or 2 numbers as appropriate.
        Raises a ValueError if a, b, or c is not a number.
    """
    try:
        if type(a) or type(b) or type(c) != int:
            raise ValueError
        if (b*b) < (4*a*c):
            raise FileExistsError
        root1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
        root2 = (-b - math.sqrt(b*b - 4*a*c))/2*a
        return [root1, root2]
    except FileExistsError:
        return []

print(roots(4,'deez',1))
