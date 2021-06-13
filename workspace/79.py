a = int(input())
#1 + 2 + 3 + .... i = a 같다면 -> print(i)
sum = 0
i = 0
while a>=i:
    i+=1
    sum += i 
    if(sum==a):
        print(i)
