Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def equilateral(sides):
    a,b,c=sides
    """Returns True if it is an equilateral triangle, otherwise return False."""
    if a==b and b==c and a!=0:
        return True
    else:
        return False
def isosceles(sides):
    a,b,c=sides
    """Returns True if it is an isosceles triangle, otherwise return False."""
    if a+b>c and b+c>a and a+c>b:
        if a==b or b==c or a==c:
            return True
        else:
            return False
    else:
        return False
def scalene(sides):
    a,b,c=sides
    """Returns True if it is an scalene triangle, otherwise return False."""
    if a+b>c and b+c>a and a+c>b:
        if a!=b and b!=c:
            return True
        else:
            return False
    else:
        return False
    