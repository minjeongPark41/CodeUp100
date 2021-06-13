i=1
sum=0
a = int(input())
# 만약 a가 5라면 짝수는 2,4 
b = a//2 # 이러면 a 안에 있는 짝수 개수를 얻을 수 있겠고
#2,4
#2(1+2+3+...b)

while b>=i:
    sum1=2*i
    sum+=sum1
    i+=1
print(sum)


sum=0
a = int(input())
for i in range(1, a+1):
    if (i%2==0):
        sum = sum+i
print(sum)


    
