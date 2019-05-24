import fileinput
# Kattis Erase Securely
# https://open.kattis.com/problems/erase
file = fileinput.input()  # defaults to sys.stdin

iterations = int(file.readline())
before = file.readline().strip()
after = file.readline().strip()

copy = ""  # comparison string

d = {'0': '1',
     '1': '0'}  # dict used to map 0 to 1, and 1 to 0

if iterations % 2 == 1:  # odd number of iterations, flip once for same effect
    copy = "".join([d.get(char) for char in before])  # get key
else:  # or not at all
    copy = before

if copy == after:
    print("Deletion succeeded")
else:
    print("Deletion failed")
