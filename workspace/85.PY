w, h, b = map(int, input().split())
storage = ((w*h*b)/8/1024/1024)
print(round(storage, 2), "MB")

w, h, b = map(int, input().split())
storage = (w*h*b)/8/1024/1024
print(format(storage,".2f"), "MB")

w, h, b = map(int, input().split())
print('%.2f'%(w*h*b/8/1024/1024), "MB")

