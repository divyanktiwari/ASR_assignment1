#10	9	the	the	3.18703103
#0	3.13813806
#1	0	man	man	7.51587486
#2	1	the	the	1.71479225
#3	2	all	all	4.55972385
#4	3	<eps>	<eps>
#5	4	for	for	3.96530032
#6	5	gate	gate	8.08131409
#7	6	the	the	1.69003808
#8	7	to	to	3.00643468
#9	8	bridge	bridge	7.91591454


file1=open('final1.txt','r')
Lines=file1.readlines()

l={}

for line in Lines:
    p=line.split()
    if(int(p[0])!=0):
        
        l[int(p[0])]=p[2]



b=l.items()
k=sorted(b)

k.reverse()

strin=""

for count,i in enumerate(k):
    if(k[count][1]!='<eps>'):
        strin=strin+k[count][1]+ " "

print(strin.strip())

