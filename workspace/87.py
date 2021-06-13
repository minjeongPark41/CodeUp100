a = int(input()) 
#1,2,3,4,5....a
for i in range(1, a+1):
    if(i%3==0):
        continue
    else:
        print(i, end=' ')