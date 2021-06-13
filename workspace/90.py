a, m, d, n = map(int, input().split())

# 1) a
# 2) a*m+d
# 3) (a*m+d)*m+d 

for i in range (1,n):
    a = a*m+d
print(a)
