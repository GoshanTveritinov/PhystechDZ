with open(r'C:\Users\Георгий\Desktop\MIPT\Первый семинар\sem1N4\input1N4.txt', 'r') as f, open(r'C:\Users\Георгий\Desktop\MIPT\Первый семинар\sem1N4\output1N4.txt', 'w') as g:
	lines = f.readlines()

	numbers = list(map(int, lines[0].split()))
	op = lines[1].strip()
	
	if op == "+":
		result = sum(numbers)

	elif op == "-":
		result = numbers[0]
		for i in numbers[1:]:
			result -= i

	elif op == "*":
		result = 1
		for i in numbers:
			result *= i

	g.write(str(result))