def flip(li):
	temp_li = []
	length = len(li)
	for i in range(length):
		temp_li.append(li[length - i - 1])
	for i in range(length):
		li.pop()
	for i in range(length):
		li.append(temp_li[i])