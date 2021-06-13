a = int(input())
# 1 2 3 .... a

for i in range(1,a+1): #ex) a=5라면 i는 1,2,3,4,5
    if(i%10==3 or i%10==6 or i%10==9):
        print("X", end=' ')
    else:
        print(i, end=' ')