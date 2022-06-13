def process(input):

    data_str  = open("one.txt").read().splitlines()
    data_int  = [int(x) for x in data_str]

    return data_int

def oneOne(input):

    increases = 0

    for i in range(1,len(input)):
        if input[i] > input[i-1]:
            increases += 1

    return increases

def oneTwo(input):

    increases = 0

    for i in range(1,len(input)-2):
        if input[i+2] > input[i-1]:
            increases += 1
            
    return increases

print(oneOne(process("one.txt")))
print(oneTwo(process("one.txt")))