import sys
file1 = open('vocab.txt', 'r')
Lines = file1.readlines()


w1=sys.argv[1]
w2=sys.argv[2]
w3=sys.argv[3]
w4=sys.argv[4]



for line in Lines:
	if(line.strip()!=w3 and line.strip()!=w4):
		print("0 0 %s %s" % (line.strip(),line.strip()))
print("0 1 %s %s" % (w3,w3))
print("0 2 %s %s" % (w4,w4))

for line in Lines:
	if(line.strip()!=w4):
		print("1 1 %s %s" % (line.strip(),line.strip()))

for line in Lines:
	if(line.strip()!=w3):
		print("2 2 %s %s" % (line.strip(),line.strip()))
	
print("2 3 %s %s" % (w3,w3))
print("1 3 %s %s" % (w4,w4))
for line in Lines:
	print("3 3 %s %s" % (line.strip(),line.strip()))
	
print(3)
