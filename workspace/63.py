a,b = map(int, input().split())
if(a>b):
    print(a)
else:
    print(b)

a, b = input().split()
a = int(a)
b = int(b)
c = (a if(a>b) else b)
print(c)