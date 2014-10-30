from random import randint

def valid_number(n):
    """
    valid_number (n)

    return False if number is invalid:
        - n is not integer
        - bigger than 987, shorter than 123
        - digits in not descending order

    otherwhise number is valid, return True
    """
    if not type(n).__name__ == 'int':
        return False
    if not 987>n>123:
        return False
    hundreds, tens, units = str(n)
    if units>=tens:
        return False
    elif tens>=hundreds:
        return False
    return True

def reverse(n):
    """
    inverse (n)

    return reverse of a 3 digits integer. For example:
    n = 952
    return value will be 259
    """
    hundreds, tens, units = str(n)
    return int(units+tens+hundreds)

def puzzle_numbers(n):
    """
    puzzle_numbers (n)

    First get the difference between "n" number and reverse(n)
    then return the sum of difference + reverse(difference)

    if "n" is valid number, puzzle_numbers function should return 1089
    otherwise code error -1 should be returned

    See help(reverse) and help(valid_number) for more information
    """
    # uncomment next lines if you're not running the tests:
    #if not valid_number(n):
    #    return -1
    hundreds, tens, units = str(n)
    difference = n - reverse(n)
    return difference + reverse(difference)

# Uncomment next lines for test:
"""
for i in range(10):
    number = 0
    while 1:
        number = randint(123, 987)
        if valid_number(number):
            break
    print "Test with: ", number
    print "Puzle returns: ", puzzle_numbers(number)
"""
