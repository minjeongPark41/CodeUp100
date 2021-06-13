a,r,n = map(int, input().split())

# 2
# 2*3
# 2*3*3
# 2*3*3*3

# 2*3**(n-1)

x = a*r**(n-1)
print(x)



result = a
a,r,n = map(int, input().split())
for i in range(1,n):
    result *=r
print(result)
