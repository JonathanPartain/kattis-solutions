import fileinput
# Kattis Genetic Search
# https://open.kattis.com/problems/geneticsearch

# Counter helper function, finds number of overlapping substring appearances
def counter(sub, full):
    count = 0
    for index in range(len(full)):  # iterate through string
        if full[index:].startswith(sub):  # start string at index i, and to the end. See if it starts with S
            count += 1
    return count


characters = ['A', 'G', 'C', 'T']

for line in fileinput.input():
    strings = line.strip().split()
    if len(strings) > 1:  # its not a zero
        S = strings[0]
        L = strings[1]
        # init all variables
        type1 = 0
        type2 = 0
        type3 = 0
        # type 1 count
        type1 = counter(S, L)

        # type 2 count
        # delete one character from S
        alternatives_del = []
        for i in range(len(S)):
            tmp = S[:i] + S[i+1:]
            alternatives_del.append(tmp)

        # remove duplicates
        alternatives_unique = list(set(alternatives_del))
        for string in alternatives_unique:
            type2 += counter(string, L)

        # type 3 count
        alternatives_add = []
        for c in characters:
            for i in range(len(S)+1):  # length of string, plus 1, so that the character can be appended
                tmp = S[:i] + c + S[i:]  # add character at every index
                alternatives_add.append(tmp)

        alternatives_unique = list(set(alternatives_add))  # re-using variable name, remove dupes
        for string in alternatives_unique:
            type3 += counter(string, L)

        print(type1, type2, type3)



