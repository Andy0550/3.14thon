
import string


file = open("raven.txt", "r", encoding="utf8")

text = ""

for x in file:
    for y in x:
        if y in string.ascii_letters:
            text += y.lower()

length = 0
for y in text:
    if len(y) == len(set(y))        
            


    
