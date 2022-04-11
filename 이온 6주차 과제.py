import math

def divide(a, b):
    ans = math.factorial(a+b)/(math.factorial(a)*math.factorial(b))
    int(ans)
    return ans

p = int(input()) 
a = b = total = ans = 0 

for b in range(100):	
    a = p - (2 * b)
    if a < 0:
      continue
    ans = divide(a,b)
    total += ans
    
print(int(total))