nums = [i for i in range(10)]
odd = []
even = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(odd, even)
