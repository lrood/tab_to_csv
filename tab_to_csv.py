import os

file = open('trial.txt', 'r', errors = 'ignore')
f = open('out.csv', 'w', errors = 'ignore')

for line in file:
	x = line
	x = (x.replace(",",""))
	x = (x.replace("\t", ","))
	f.write(x)
file.close()
f.close()
