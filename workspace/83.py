r, g, b = map(int, input().split())
for i in range(0, r):
    for x in range(0, g):
        for y in range(0, b):
            print(i,x,y)
print(int(r*g*b))
