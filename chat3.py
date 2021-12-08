lines = []
with open('3.txt', 'r' , encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line)
print(lines)
new = []
for line in lines:
	s = line.strip('\n').split(' ')
	time = s[0][:5]
	name = s[0][5:]
	if name == 'Viki':
		a = ('Viki:' + str(line[9:].strip('\n')))
	elif name == 'Allen':
		a = ('Allen:' + str(line[10:].strip('\n')))
	new.append(a)
print(new)

