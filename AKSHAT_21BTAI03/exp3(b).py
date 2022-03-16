num=input('Enter number:')
n=list(num)

len_num=len(n)
sum=0
for i in range(len_num):
    sum+=pow(int(n[i]),len_num)

if(int(num)==sum):
    print("It is armstrong")
else:
    print("It is not armstrong")