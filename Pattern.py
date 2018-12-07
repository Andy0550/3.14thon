# Michael Dvořák
# Python_3.7.0

def patt(line,p):
    i=0
    pat=line
    for x in range(len(pat)):
        if pat[x].isalpha():
            pat=pat.replace(pat[x],str(i),pat.count(pat[x]))
            i += 1
        if pat == p:
            print(line,end=",")

p = "012324567"
print(p,"\n")

with open ("/Users/Michael/Desktop/dictionary.txt", "r") as f:
    for line in f:
        patt(line.rstrip("\n"),p)



