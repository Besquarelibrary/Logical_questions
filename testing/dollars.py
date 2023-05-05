s='d50,p70,80d,p50,d20'
list=s.split(',')
dollar=0
for i in list:
	if 'd' in i:
		s=i.strip('d')
		dollar=dollar+int(s)
print(dollar)