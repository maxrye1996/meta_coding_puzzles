from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  deflate_count: int = 0
  previous_value: int = 0
  current_value: int = 0
  
  # loop R backwards
  for i in range(N - 1, 0, -1):
    previous_value = R[i - 1]
    current_value = R[i]
    if previous_value >= current_value:
      previous_value = current_value - 1
      if previous_value <= 0:
        return -1
      R[i - 1] = previous_value
      deflate_count += 1

  return deflate_count



N = 5
R = [2, 5, 3, 6, 5]
print(getMinimumDeflatedDiscCount(N,R))

N = 3
R = [100, 100, 100]
print(getMinimumDeflatedDiscCount(N,R))

N = 4
R = [6, 5, 4, 3]
print(getMinimumDeflatedDiscCount(N,R))