from random import randint as rd

radky=rd(10,20)
sloupce=rd(10,20)
for x in range(radky): 
    for y in range(sloupce):
        print(rd(0,999),end="\t")
    
    
