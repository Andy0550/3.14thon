# Michael Dvořák
# Python_3.7.0

def B2B(inp,start,end):
    x = int(inp,start)
    arr = []
    table = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while(x != 0):
        arr.append(table[x%end])
        x = x // end
    for i in reversed(arr):
        print(i,end="")


print("Please enter number, input base and output base. \n")
x = input("Number:")
y = int(input("Input Base:"))
z = int(input("Output Base:"))
B2B(x,y,z)
