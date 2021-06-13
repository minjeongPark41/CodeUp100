a,b,c = map(int, input().split())
#3,7,9 -> 3,7,3

day=1
# while day%a==0 and day%b==0 and day%c==0:
while day%a!=0 or day%b!=0 or day%c!=0:
    day+=1
print(day)
