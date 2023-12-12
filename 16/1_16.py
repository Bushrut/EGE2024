r = {1:5}

for n in range(2, 2025):
    r[n] = 2*n +1 + r[n-1]

print(r[2024] - r[2022])