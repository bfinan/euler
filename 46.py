next_tri = 0

UPPER_BOUND = 100000

def get_tris(bound):
    tris = []
    for n in range(1, bound):
        tris.append(int((n*(n+1))/2))
    return tris

def get_pentas(bound):
    pentas = []
    for n in range(1, bound):
        pentas.append(int((n*(3*n-1))/2))
    return pentas

def get_hexas(bound):
    hexas = []
    for n in range(1, bound):
        hexas.append(int((n*(2*n-1))))
    return hexas

tenktris = get_tris(UPPER_BOUND)
tenkpentas = get_pentas(UPPER_BOUND)
tenkhexas = get_hexas(UPPER_BOUND)
print(tenkhexas[0:5])
print(tenkpentas[0:5])



for tri in tenktris:
    if tri <= 40755:
        continue
    if tri in tenkpentas and tri in tenkhexas:
        next_tri = tri 
        print(f"trihexapenta found: {tri}")
        break


print(f"Answer: {next_tri}")