
file1 = open('vocab.txt', 'r')
Lines = file1.readlines()

with open('z.txt','r') as file:
        str2=file.readline()

str3=str2[1:-1]
str1=str3[:-1]
x= str1.split()

length=len(x)

k=0
i=0
while(x[i] != 'XXX'):

	print("%s %s %s %s" % (i,i+1,x[i],x[i]))
	i=i+1
for line in Lines:
        print("%s %s XXX %s" % (i,i+1,line.strip()))
i=i+1
while(i<length):
	print("%s %s %s %s" % (i,i+1,x[i],x[i]))
	i=i+1

print(i)
