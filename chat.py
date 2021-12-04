

def read_file(filename):
	lines = []
	with open(filename,'r',encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())	
	print(lines)
	return lines


def convert(lines):	
	new = []
	person = None
	for line in lines:
		if line == 'Tom':
			person = 'Tom'
			continue
		elif line == 'Allen':
			person = 'Allen'
			continue
		if person:
			new.append(person + ':' + line)
	print(new)
	return new

def write_file(filename , lines):
	with open(filename, 'w' ,encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')






def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt' , lines)

main()