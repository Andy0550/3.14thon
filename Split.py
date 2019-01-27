# Michael Dvořák
# Python_3.7.0

def isPrime(x):
    if(x == 0 or x == 1):
        return False
    return all(x % i != 0 for i in range (2,x))


def Split(num):
    c = ""
    v = ""
    a = 3
    while True:
        if(a < 1):
            print("No prime numbers found")
            break
        for x in num:
            c += x
            if(len(c) == a):
                if(isPrime(int(c))):
                    v += (c + ",")
                    c = ""
                else:
                    v += c
                    c = ""
        try:            
            if(isPrime(int(c))):
                v += ("," + c)
                c = ""
            else:
                v += c
                c = ""
        except:
            pass
            
        if("," in v):
            print(v.split(","))
            break
        else:
            a -= 1
            v = ""
        

#Split("9027163345724111111")
#Split("999999999999999")
#Split("908164432136316265231245")
Split("9027163345724111111")



