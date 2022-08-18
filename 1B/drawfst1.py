import sys
file1 = open('vocab.txt', 'r')
Lines = file1.readlines()

w1=sys.argv[1]
w2=sys.argv[2]
w3=sys.argv[3]
w4=sys.argv[4]



for line in Lines:
	if(line.strip()!=w1 and line.strip()!=w2):
		print("0 0 %s %s" % (line.strip(),line.strip()))
print("0 1 %s %s" % (w1,w1))

for line in Lines:
	if(line.strip()!=w2):
		print("1 1 %s %s" % (line.strip(),line.strip()))
	
print("1 2 %s %s" % (w2,w2))

for line in Lines:
	if(line.strip()!=w1):
		print("2 2 %s %s" % (line.strip(),line.strip()))
	
print(2)
