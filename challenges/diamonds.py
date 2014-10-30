def create_diamond(n, filled=True):
    """
    create_diamond(n, filled=True)

    It will create (print) a diamond in accordance with number n and can be filled or not.
    This is an example from n=5

    filled = True
            *
           * *
          * * *
         * * * *
        * * * * *
         * * * *
          * * *
           * *
            *

    filled = False
            *
           * *
          *   *
         *     *
        *       *
         *     *
          *   *
           * *
            *
    """
    for i in range(1, n*2):
        if filled:
            if i<=n:
                print " "*(n-i) + "*" + (" " + "*")*(i-1)
            else:
                print " "*(i-n) + "*" + (" " + "*")*(n*2-i-1)
        else:
            if i<=n:
                value = " "*(n-i) + "*" + (" ")*(i-1)*2
                print value[:-1] + "*"
            else:
                value = " "*(i-n) + "*" + (" ")*(n*2-i-1)*2
                print value[:-1] + "*"


# Uncomment next lines for test:
"""
import random
for i in range(5):
    number = random.randint(0, 10)
    filled = bool(random.getrandbits(1))
    print "Test with: ", number, "filled = ", filled
    create_diamond(number, filled)
"""
