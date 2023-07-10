import sys

N = int(sys.stdin.readline())
MaxS = 0
MinC = 51
MinL = 180

result = 0

for i in range(N):
    S, C, L = map(int, input().split())
    if S > MaxS :
        MaxS = S
        MinC = C
        MinL = L
        result = i + 1
    
    if S == MaxS:
        if C < MinC:
            MaxS = S
            MinC = C
            MinL = L
            result = i + 1
        
        elif C == MinC:
            if L < MinL:
                MaxS = S
                MinC = C
                MinL = L
                result = i + 1

print(result)