def process(input):

    data_str  = open("two.txt").read().splitlines()
    return data_str

def twoOne(input):

    posH = 0
    posV = 0

    for line in input:
        direction = line.split(" ")
        if direction[0]=="forward":
            posH += int(direction[1])
        if direction[0]=="up":
            posV -= int(direction[1])
        if direction[0]=="down":
            posV += int(direction[1])
    
    return posH * posV

def twoTwo(input):

    posH = 0
    posV = 0
    aim  = 0

    for line in input:
        direction = line.split(" ")
        if direction[0]=="forward":
            posH += int(direction[1])
            posV += aim*int(direction[1])
        if direction[0]=="up":
            aim -= int(direction[1])
        if direction[0]=="down":
            aim += int(direction[1])

    return posH * posV

print(twoOne(process("two.txt")))
print(twoTwo(process("two.txt")))
