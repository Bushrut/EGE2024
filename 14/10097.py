n = 3*3125**8+2*625**7-4*625**6+3*125**5-2*25*4-2024
res = []
counter = 0
while  n > 0:
    if n%25 == 0:
        counter += 1
    res = [n%25] + res
    n = n//25
print(counter)

