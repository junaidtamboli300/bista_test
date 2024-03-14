## sum of n numbers 

def sum(n):
    ans = 0
    total = 0
    for i in range(11):
        ans = i + ans
    return ans

print(sum(10))