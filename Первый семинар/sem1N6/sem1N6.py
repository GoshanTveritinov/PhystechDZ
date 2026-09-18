with open(r'C:\Users\Георгий\Desktop\MIPT\Первый семинар\input.txt', 'r') as f, open(r'C:\Users\Георгий\Desktop\MIPT\Первый семинар\output.txt', 'w') as g:
	lines = f.readlines()

	numbers = list(map(int, lines[0].split()))
	op = lines[1].strip()
	sys = int(lines[2])
	sum10 = 0

	for n in numbers:
		n = str(n)
		n10 = 0
		l = len(n)
		N = n[::-1]
		for i in range(l):
			a = N[i]
			n10 += int(a) * (sys**i)
		sum10 += n10

	result = ''
	while sum10 >= sys:
		ostatok = sum10 % sys
		sum10 = sum10 // sys
		result += str(ostatok)
	result = result + str(sum10)
	
	g.write(result[::-1])
