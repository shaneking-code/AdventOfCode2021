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

def threeTwo(input):

    oxy = ""
    car = ""

    gam,eps = getGamEps(input)

    if gam in input:
        oxy = gam
    if eps in input:
        car = eps

    
    return input
                

                
                

print(threeOne(process("three.txt")))