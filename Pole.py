import random

pole = []
for i in range (0,1000):
    pole.append(random.randint(-100,100))

for i in (pole):
    if i < 0 and i%2 == 0:
        print(i) 
