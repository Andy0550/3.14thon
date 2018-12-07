# Michael Dvořák
# Python_3.7.0

import random as rd
import string

#Password_1
def isPrime(cislo):
    return all(cislo % i != 0 for i in range (2,cislo))

for x in range(1000,9999):
    a = str(x)
    a_1 = int(a[0])
    a_2 = int(a[1])
    a_3 = int(a[2])
    a_4 = int(a[3])
    if x % 7 != 0 and a_3 == a_4 + a_2 and (a_1*10) + a_2 == 15*a_4 and isPrime(a_1*10 + a_4):
        print(x,"\n")


#Password_2
password = []
for x in range(10):
    password.append(0)


while True:
    p0=rd.choice(string.ascii_lowercase)
    p1=rd.choice(string.ascii_lowercase)
    if p0 != p1:
        break

while True:
    p2=rd.choice(string.ascii_uppercase)
    p3=rd.choice(string.ascii_uppercase)
    if p2 != p3:
        break
    
while True:
    p4=rd.choice(string.punctuation)
    p5=rd.choice(string.punctuation)
    p6=rd.choice(string.punctuation)
    if p4 != p5 and p5 != p6 and p4 != p6:
        break
    
while True:
    p7=str(rd.randint(0,9))
    p8=str(rd.randint(0,9))
    p9=str(rd.randint(0,9))
    if p7 != p8 and p8 != p9 and p7 != p9:
        break
  
#UpperCase
a = rd.randint(1,2)
password[a] = p2
password[7-a] = p3
#LowerCase
password[a-1] = p0
password[7-a-1] = p1
#Punctuation
for x in range(4,10):
    if password[x] == 0:
        password[x] = p4
        break

for x in range(4,10):
    if password[x] == 0:
        password[x] = p5
        break

for x in range(4,10):
    if password[x] == 0:
        password[x] = p6
        break
#Numbers
for x in range(0,10):
    if password[x] == 0:
        password[x] = p7
        break

for x in range(0,10):
    if password[x] == 0:
        password[x] = p8
        break

for x in range(0,10):
    if password[x] == 0:
        password[x] = p9
        break

print("".join(password),end="")
