# Michael Dvořák
# Python_3.7.0

x = 1
while x == 1:
    try:
        c=int(input("Enter number of rows: "))
        if c == 0:
                print("Ending....")
                break       
        print("(Press 0 to end)" "\n")
    except ValueError:
        print("Wrong input. Try Again !!!" "\n")
        continue
    p=[]
    for i in range(c):
        p.append([])
        p[i].append(1)
        for j in range(1,i):
            p[i].append(p[i-1][j-1]+p[i-1][j])
        if(c!=0):
            p[i].append(1)
    for i in range(c):
        print("   "*(c-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(p[i][j]),end=" ",sep=" ")
        print("\n")
