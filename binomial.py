assert type(n) == int
assert n > 0

import doctest
import math
def logfactorial(n):
    """
    calcualtes log factoria
    >>>int(logfactorial(10))
    15
    """
    logbi = 0
    for i in range(1,n+1):
        logbi = logbi + math.log(i)
    return logbi
