count = 1
am = 0
for i in range(0, 16777216):
    am += 1
    if '11' in str(bin(i)):
        count += 1
print(count)
print(am)
print(am - count)