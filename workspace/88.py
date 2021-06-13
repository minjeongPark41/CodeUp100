# a=1
# d=3
# n=123

# 1) 1
# 2) 1+3
# 3) (1+3)+3
# 4) (1+3+3)+3
# n번째) 1+3(n-1)

a,d,n = map(int, input().split())
x = int(a+(n-1)*d)
print(x)
