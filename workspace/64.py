a,b,c = map(int, input().split())
d = (a if(a<b) else b)
e = (d if(d<c) else c)
print (e)

a,b,c = map(int, input().split())
print(min(a,b,c))