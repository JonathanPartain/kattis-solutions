import fileinput
# Kattis Bit by Bit
# https://open.kattis.com/problems/bitbybit

file = fileinput.input()  # defaults to sys.stdin


def clear_byte(byte_str, index):
    byte_str[int(index)] = "0"
    return byte_str


def set_byte(byte_str, index):
    byte_str[int(index)] = "1"
    return byte_str


def and_byte(byte_str, index_0, index_1):
    val_0 = byte_str[int(index_0)]
    val_1 = byte_str[int(index_1)]
    if val_1 == "1" and val_0 == "1":  # if both are true
        byte_str[int(index_0)] = "1"  # set to 1
    elif val_0 == "0" or val_1 == "0":  # if either is false
        byte_str[int(index_0)] = "0"  # set to 0
    else:
        byte_str[int(index_0)] = "?"  # otherwise, we don't know
    return byte_str


def or_byte(byte_str, index_0, index_1):
    val_0 = byte_str[int(index_0)]
    val_1 = byte_str[int(index_1)]
    if val_0 == "1" or val_1 == "1":  # if either is true
        byte_str[int(index_0)] = "1"  # set to true
    elif val_0 == "0" and val_1 == "0":  # if both are false
        byte_str[int(index_0)] = "0"  # set to false
    else:
        byte_str[int(index_0)] = "?"  # otherwise we don't know

    return byte_str


instruction = {
    "CLEAR": clear_byte,
    "SET": set_byte,
    "OR": or_byte,
    "AND": and_byte
}


for instructions in file:
    instructions = int(instructions)  # set instructions to an integer
    byte_rep = "????????????????????????????????"  # create string representation of byte
    byte_rep = list(byte_rep)  # turn into a list
    if instructions == 0:  # if instruction is 0, break
        break
    for j in range(instructions):  # for every instruction
        inst_arr = file.readline().strip().split()  # get a line, turn into a list
        if len(inst_arr) == 2:  # set and clear functions are 2 long
            inst = inst_arr[0]
            byte_rep = instruction[inst](byte_rep, inst_arr[1])  # call instruction inst, with byte_rep and arguments
        else:  # or and and functions are 3 long
            inst = inst_arr[0]
            byte_rep = instruction[inst](byte_rep, inst_arr[1], inst_arr[2])

    # reverse list
    byte_rep = byte_rep[::-1]
    # turn into string
    byte_rep = "".join(byte_rep)
    print(byte_rep)


