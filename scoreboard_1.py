from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    # Write your code here
    # find max number of games:
    S.sort()
    count: int = S[-1] // 2
    
    # find if we need a one:
    need_one: int = 0
    for score in S:
        if score % 2 == 1:
            need_one = 1
            break
    return count + need_one


N = 6
S = [1, 2, 3, 4, 5, 6]
print(getMinProblemCount(N,S))