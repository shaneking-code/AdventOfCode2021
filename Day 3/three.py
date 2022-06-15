def process(input):

    data_str  = open("three.txt").read().splitlines()
    return data_str[1:]

def threeOne(input): #some changes
    
    gam,eps = getGamEps(input)
    return int(gam,2)*int(eps,2)

def getGamEps(input):

       
    gam = ""
    eps = ""

    for i in range(len(input[0])):

        sum = 0

        for line in input:

            if line[i]=='1':

                sum += 1

        if sum > len(input)//2:

            gam += '1'
            eps += '0'

        else:
            
            eps += '1'
            gam += '0'

    return gam,eps     

def validate(index,l,val):
    y = list(filter(lambda x: x[index]==val,l))
    return y

def getMostCommonCar(index,l):
    sum = 0
    for line in l:
        if line[index]=='1':
            sum += 1
    if sum >= len(l)//2: #
        return '1'
    else:
        return '0'

def getMostCommonOxy(index,l):
    sum = 0
    for line in l:
        if line[index]=='1':
            sum += 1
    if sum < len(l)//2: #
        return '1'
    else:
        return '0'

def threeTwo(input,i,oxy):
    if len(input)==1 or i==len(input[0]):
        return input[0]
    else:
        if oxy:
            val = getMostCommonOxy(i,input)
        else:
            val = getMostCommonCar(i,input)

        input = validate(i,input,val)
        return threeTwo(input,i+1,oxy)

print(threeOne(process("three.txt")))
print(int(threeTwo(process("three.txt"),0,True),2) * int(threeTwo(process("three.txt"),0,False),2))
