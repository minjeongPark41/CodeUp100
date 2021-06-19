n = int(input())
a = input().split()

#a[0]=?, a[1]=?,....a[n-1]=?

for i in range(n):
    a[i] = int(a[i])

# for i in range(n):
#     print(a[i], end=' ')

# 이거를 거꾸로 어떻게 출력할 수 있을까 

# for i in range(n):
#     a[n-i-1] = a[i]

# a[0] = 1    a[n-1] = 2 
# a[1] = 3    a[n-2] = 4


for i in range(n):
    print(a[n-i-1], end=' ')