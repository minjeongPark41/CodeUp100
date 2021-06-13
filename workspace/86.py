a = int(input()) #ex) 57
# 1+2+3+...n = b (b<a일때까지만)n
sum=0
for i in range(1, a+1): #i는 1,2,3...
    sum+=i
    if(sum>a):
        break
print(sum)

a = int(input())
i=0
sum=0
while True:
    i+=1
    sum+=i
    if(sum>a):
        break
print(sum)
