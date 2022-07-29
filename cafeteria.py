from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here

    if int(N / (K + 1)) == M:
        return 0
    
    S.sort()
    available_seats: int = 0
    
    for a, b in zip([-K] + S, S + [N + K + 1]):
        available_seats += int((b - a) / (K + 1)) - 1
    
    return available_seats
    



N = 15
K = 2
M = 3
S = [11, 6, 14]
print(getMaxAdditionalDinersCount(N,K,M,S))