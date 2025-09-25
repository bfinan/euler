import math

TOP_LIM = 987654322



def is_prime(i):
    if i == 1:
        return False
    for j in range(2, int(math.sqrt(i) +1)):
        if i % j == 0:
            return False
    return True

def is_pandigital(prime):
    strprime = str(prime)
    n = len(strprime)
    for i in range(1,n+1):
        stri = str(i)
        if stri not in strprime:
            return False
    return True

largest_found = 2


assert(is_prime(4)== False)
assert(is_prime(9)== False)


if True:
    for dog in range(33,TOP_LIM):
        if dog % 1000000 == 0:
            print(f"checking {dog}")
        if is_prime(dog):
            if is_pandigital(dog):
                largest_found = dog 
                print(f"new largest pp found: {dog}")


print(f"Answer: {largest_found}")