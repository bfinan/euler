bigstring = ""
curr_int = 1
answer = 1

ds = [1, 10, 100, 1000, 10000, 100000, 1000000]

while len(bigstring) < 1000002:
    if curr_int % 10000 == 0:
        print(f"curr_int {curr_int}")
    bigstring += str(curr_int)
    curr_int += 1


for d in ds:
    answer = answer * int(bigstring[d-1])

print(f"Answer: {answer}")