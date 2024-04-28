"""Generator bilangan pseudorandom dengan algoritma linear congruential generator
        
        Fungsi
            randrange(a, b) -> int      : memberikan integer acak di interval [a,b)
            randint(a, b) -> int        : memberikan integer acak di interval [a,b]
            randfloat(a, b) -> float    : memberikan float acak di interval [a,b]
"""   

def lcg(seed, a, c, modulus):
    val = seed
    def gen():
        nonlocal val
        val = (a*val + c)%modulus
        return val
    return gen