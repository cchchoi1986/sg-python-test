def init_format(s):
	arr = [];
	for i in range(len(s)):
		if (s[i] != '.'):
			arr.append([s[i]])
		else:
			arr.append([])
	return arr

def format_line(string):
	line = '';
	for i in range(len(string)):
		char = '.'
		if (string[i] != []):
			char = 'X'
		line = line + char;
	return line

def move(str):
	moved = []
	for i in range(len(str)):
		moved.append([])

	for i in range(len(str)):
		if (str[i] != []):
			for j in range(len(str[i])):
				value = str[i][j]
				if (value == 'R' and (i + 1) < len(str)):
					moved[i + 1].append(str[i][j])
				if (value == 'L' and (i - 1) >= 0):
					moved[i - 1].append(str[i][j])
	return moved


def animate(time, str):
	timeline = [];
	str = init_format(str)
	while (format_line(str) != '.' * len(str)):
		timeline.append(format_line(str))
		str = move(str)
	count = 0
	result = [];
	for k in timeline:
		if (count % time == 0):
			result.append(k)
		count = count + 1
	result.append('.' * len(str))
	return result

# answer = animate(2, "..R....")
# answer = animate(3, "RR..LRL")
# answer = animate(2, "LRLR.LRLR")
# answer = animate(10, "RLRLRLRLRL")
# answer = animate(1, "...")
answer = animate(1, "LRRL.LR.LRR.R.LRRL.")

for n in answer:
	print(n)