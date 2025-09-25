import math 

min_d = 0

def gen_pentagons(maxval):
    pentas = []
    for n in range(1, maxval+1):
        pentas.append(int((n * (3 * n - 1))/2))
    return pentas 

a_thousand_pentas = gen_pentagons(10000)

assert(35 in a_thousand_pentas)
assert(145 in a_thousand_pentas)

for j in a_thousand_pentas:
    for k in a_thousand_pentas:
        if j == k:
            pass
        elif not abs(j+k) in a_thousand_pentas:
            #print(f"{j} + {k} = {j+k} not in pentas")
            pass
        elif not abs(j-k) in a_thousand_pentas:
            #print(f"{j} - {k} = {abs(j-k)} not in pentas")
            pass
        else:
            min_d = abs(j-k)
            print(f"new pentapair found: {j} + {k} = {j+k}, {j} - {k} = {abs(j-k)}")

print(f"Answer: {min_d}")