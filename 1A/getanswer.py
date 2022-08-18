file1=open('final.txt','r')
Lines=file1.readlines()
flag=0
for line in Lines:
    x=line.split()
    for count,i in enumerate(x):
        if(i=='XXX'):
            print(x[count+1])
            flag=1
            break
    if(flag==1):
        break

