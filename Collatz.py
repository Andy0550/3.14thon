n = 27
list = []
while True:
    if n==1:
        break
    if n%2 == 0:
        n=n/2
        print(n)
        list.append(n)
    else:
        n=3*n+1
        print(n)
        list.append(n)
print (len(list), end = " ")


    
