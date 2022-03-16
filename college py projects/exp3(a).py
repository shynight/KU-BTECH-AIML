number=(list(map(int,input().split())))
length_num=len(number)
l1=list()
l2=list()
for i in range(length_num):
    if(number[i]%2==0):
        l1.append(number[i])
    else:
        l2.append(number[i])
print("The even number are {} \nThe odd number are {}".format(l1,l2))