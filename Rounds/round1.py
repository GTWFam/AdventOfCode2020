def puzzle1(map):
	for n in map:
		if (2020 - n) in map.keys():
			print(n * (2020 - n))
			return

def puzzle2(map):
	for n in map:
		x = 2020 - n
		for k in map:
			if (x - k) in map.keys():
				print(n * (x - k) * k)
				return

file = open('../inputs/numbers.txt', 'r')
map = {}
Lines = file.readlines()
for line in Lines:
	map[int(line.strip())] = line.strip()

puzzle2(map)