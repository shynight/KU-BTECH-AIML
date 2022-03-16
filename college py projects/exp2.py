cor = input().split()
x1=int(cor[0])
x2=int(cor[1])
y1=int(cor[2])
y2=int(cor[3])
a=(x2-x1)**2
b=(y2-y1)**2
dist=(a+b)**.5
print("distance between two points is: ",round(dist,3))