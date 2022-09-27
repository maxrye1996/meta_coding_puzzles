# Write any import statements here
import itertools

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
    counter: int = 0
    
    for i, j, k in itertools.combinations(range(N), 3):

        if X <= abs(i - j) <= Y and X <= abs(j - k) <= Y:
            if (C[i] == 'P' and C[j] == 'A' and C[k] == 'B') or (C[i] == 'B' and C[j] == 'A' and C[k] == 'P'):
                counter += 1

    return counter

N = 5
C = "APABA"
X = 1
Y = 2
print(getArtisticPhotographCount(N,C,X,Y))

N = 5
C = "APABA"
X = 2
Y = 3
print(getArtisticPhotographCount(N,C,X,Y))

N = 8
C = ".PBAAP.B"
X = 1
Y = 3
print(getArtisticPhotographCount(N,C,X,Y))