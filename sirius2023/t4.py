def calculate_min_button_presses(N, K, P, U):
    if P < U:
        return min((N - P) // K + 2, (U - 1) // K + 1)
    else:
        return min((P - 1) // K + 2, (N - U) // K + 1)

N = int(input())
K = int(input())
P = int(input())
U = int(input())

result = calculate_min_button_presses(N, K, P, U)

print(result)
