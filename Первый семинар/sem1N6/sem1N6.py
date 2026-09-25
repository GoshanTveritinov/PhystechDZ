with open(r'C:\Users\Георгий\Desktop\MIPT\Первый семинар\sem1N6\input1N6.txt', 'r') as f, open(r'C:\Users\Георгий\Desktop\MIPT\Первый семинар\sem1N6\output1N6.txt', 'w') as g:
	lines = f.readlines()

	numbers = list(map(int, lines[0].split()))
	op = lines[1].strip()
	sys = int(lines[2])
	res10 = 0
	numbers10 = []

	for n in numbers:
		n = str(n)
		n10 = 0
		l = len(n)
		N = n[::-1]
		for i in range(l):
			a = N[i]
			n10 += int(a) * (sys**i)
		numbers10.append(n10)
			
	print(numbers10)

	if op == "+":
		result10 = sum(numbers10)
	
	elif op == "-":
		result10 = numbers10[0]
		for i in numbers10[1:]:
			result10 -= i
	
	elif op == "*":
		result10 = 1
		for i in numbers10:
			result10 *= i

	result10str = str(result10)
	print(result10str)
	
	val = 0
	if result10 > 0:
		for i in range(len(result10str)):
			val += (int(result10str[-i-1]) * 10**i)
		res = " "
		while(val>0):
			res += str(val%sys)
			val = val // sys
		

	else:
		for i in range(len(result10str)-1):
			val += (int(result10str[-i-1]) * 10**i)
		res = " "
		while(val>0):
			res += str(val%sys)
			val = val // sys
		res = res + "-"
	

	print(res[::-1])
	g.write(res[::-1])