a,b = map(int, input().split())
a = bool(a)
b = bool(b)
if(a!=b):
    print("True")
else:
    print("False")

a, b = input().split()
print(bool(int(a))!=bool(int(b)))

a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(c&(not d) | (not c)&d)