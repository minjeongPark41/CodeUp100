a, b = map(int, input().split())
a = bool(a)
b = bool(b)
if(a&b == True):
    print("True")
else:
    print("False")

a,b = input().split()
print(bool(int(a)) and bool(int(b)))