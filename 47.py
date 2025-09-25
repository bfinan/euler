import math

def get_primes(toplim):
    list_of_primes = []
    for i in range(2,toplim):
        if is_prime(i):
            list_of_primes.append(i)
    return list_of_primes

def get_dubsquares(toplim):
    list_of_dubsquares = []
    for i in range(1, toplim):
        list_of_dubsquares.append(2*(i*i))
    return list_of_dubsquares

def is_prime(n):
    if n == 1:
        return False
    else:
        for j in range(2,int(math.sqrt(n)+1)):
            if n % j == 0:
                return False
    return True

assert(is_prime(4)== False)
assert(is_prime(9)== False)
UPPER_BOUND = 100000

primes = get_primes(10000)
dubsquares = get_dubsquares(1000)

gb_candidate = 5
gb_finalist = 0

if True:
    while gb_candidate < UPPER_BOUND:
        looking_for_gb = True
        gb_candidate += 2
        if is_prime(gb_candidate):
            pass 
        else:
            # composite number
            for prime in primes:
                if looking_for_gb:
                    for dubsquare in dubsquares:
                        if dubsquare > gb_candidate or prime > gb_candidate:
                            break
                        else:
                            if prime + dubsquare == gb_candidate:
                                print(f"{gb_candidate} = {prime} + {dubsquare}")
                                looking_for_gb = False 
                                break
            if looking_for_gb:
                gb_finalist = gb_candidate
                break



print(f"Answer: {gb_finalist}")