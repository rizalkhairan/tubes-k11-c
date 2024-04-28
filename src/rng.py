"""Generator bilangan pseudorandom dengan algoritma linear congruential generator
        
        Fungsi
            randrange(a, b) -> int      : memberikan integer acak di interval [a,b)
            randint(a, b) -> int        : memberikan integer acak di interval [a,b]
            randfloat(a, b) -> float    : memberikan float acak di interval [a,b]
"""   

import time

# Parameter didapatkan dari paper https://www.ams.org/journals/mcom/1999-68-225/S0025-5718-99-00996-5/S0025-5718-99-00996-5.pdf 
M = 17179869143  # 2**34 - 41
A = 473186378
C = 0

def lcg(seed=None, a=A, c=C, modulus=M):
    if seed is None:
        seed = int(time.time())
    
    val = seed
    def gen():
        nonlocal val
        val = (a*val + c)%modulus
        return val
    return gen

random = lcg()

def uniform():
    return random()/M


def randfloat(a, b):
    return a + (b - a)*uniform()