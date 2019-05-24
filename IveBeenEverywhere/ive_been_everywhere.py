import fileinput
# Kattis I've Been Everywhere, Man
# https://open.kattis.com/problems/everywhere

file = fileinput.input()  # defaults to sys.stdin
numTests = file.readline().strip()  # grabs first line, representing number of test cases

for i in range(int(numTests)):
    cities = file.readline().strip()  # number of cities visited during trip i
    out = set()  # store number of cities as a set, as sets cannot contain duplicates
    for j in range(int(cities)):  # iterate over number of cities
        city = file.readline().strip()
        out.add(city)
    print(len(out))


