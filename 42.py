

def get_triangles(upperlimit):
    trilist = []
    for n in range(1, upperlimit):
        trilist.append(int((0.5 * n)*(n+1)))
    return trilist


def get_letter_value(charchar):
    return ord(charchar)-64

assert(get_letter_value('A')== 1)
assert(get_letter_value('Z')== 26)

big_tri_list = get_triangles(200)

triangle_words = 0
with open("0042_words.txt", 'r') as f:
    bigstring = f.read()
    allwords = bigstring.split(",")
    striwords = []
    #allwords_stripped = allwords.strip('"') for word in allwords
    for word in allwords:
        striwords.append(word.strip('"'))
    print(striwords)

for striword in striwords:
    tritotal = 0
    for strichar in striword:
        tritotal += get_letter_value(strichar)
    if tritotal in big_tri_list:
        triangle_words += 1

answer = triangle_words

print(f"Answer: {answer}")