h, b, c, s = map(int, input().split())
# 필요한 저장공간
a = int(h*b*c*s)
print(format(a/8/1024/1024, ".1f"), "MB")

h, b, c, s = map(int, input().split())
print(round(h*b*c*s/8/1024/1024,1), "MB")