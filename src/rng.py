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

def lcg(seed, a, c, modulus):
    def gen():
        gen.value = (a*gen.value + c) % modulus
        return gen.value
    gen.value = seed
    return gen

random = lcg(int(time.time()), A, C, M)

def uniform():
    return random()/M


def randrange(a, b):
    return a + int((b - a)*uniform())

def randint(a, b):
    return randrange(a, b+1)

def randfloat(a, b):
    return a + (b - a)*uniform()