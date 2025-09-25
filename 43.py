import math

TOP_LIM = 9976543091
first_primes = [2, 3, 5, 7, 11, 13, 17,]

def is_pandigital(l):
    strint = str(l)
    for i in range(0, len(strint)):
        if str(i) not in strint:
            return False
    return True

def is_pansubprime(m):
    z_index = 0
    for z in range(1,len(str(m))-2):
        #print(str(m)[z:z+3])
        substring = str(m)[z:z+3]
        if int(substring) % first_primes[z_index] != 0:
            return False
        z_index += 1
    return True

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True 
    
assert(is_prime(3))
assert(is_prime(9) == False)
assert(is_pandigital(1234567890))
assert(is_pandigital(3333333) == False)
assert(is_pansubprime(1406357289))

if True:
    total_pansubprimes = 0
    for k in range(1234567890 -1, TOP_LIM):
        if is_pandigital(k):
            if is_pansubprime(k):
                print(f"new PSP found: {k}")
                total_pansubprimes += 1

print(f"Answer: {total_pansubprimes}")