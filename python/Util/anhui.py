resArr = []
with open('file1.txt', mode='r', encoding='utf-8') as f:
	for line in f:
		arr = line.split()
		resArr.append(arr[1])
temp = []
with open("anhuiRes.txt", mode='w', encoding="utf-8") as f:
	pass
for res in resArr:
	if len(temp) != 5:
		temp.append(res)
	else:
		with open("anhuiRes.txt", mode='a', encoding="utf-8") as f:
			f.write('"{}",\n'.format('","'.join(temp)))
		temp = []
		temp.append(res)
with open("anhuiRes.txt", mode='a', encoding="utf-8") as f:
	f.write('"{}"'.format('","'.join(temp)))


