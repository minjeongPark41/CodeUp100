a,b = map(int, input().split())
a = bool(a)
b = bool(b)
if(a&b == False):
    print("True")
else:
    print("False")

a,b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a&b==False)

print(not(a|b))