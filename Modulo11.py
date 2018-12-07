# Michael Dvořák
# Python_3.7.0


def modulo11(n):
    if len(str(n)) > 10:
        return False
    digits = [int(x) for x in str(n)]
    weights = [6,3,7,9,10,5,8,4,2,1]
    c = 0
    d = 0
    for x in range(10):
        try:
            c = digits[x] * weights[x] 
            d += c
        except:
            continue
    
    if(d%11 == 0):
        return True
    else:
        return False

out = open("hw11_dvorak.txt", "w", encoding="utf8")

with open ("/Users/Michael/Desktop/accounts.txt", "r") as source:
    for line in source:
        number = int(line[0:-6])
        if (modulo11(number) == True):
            out.write(line) 
 
out.close()



