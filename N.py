import random
from math import factorial

n = 1
for i in range(1,100):
    n += 1 / i
print(n)

for i in range(10):
    x = int(random.random()*10)
    y = int(random.random()*10)
    print(f'What is {x} * {y}')
