res = []
with open('file.txt', mode='r', encoding="utf-8") as f:
    for line in f:
        arr = line.split(' ')
        res.append(arr[1])
print("一共{}个".format(len(res)))
temp = []
print_arr = []
for r in res:
    if len(temp) != 5:
        temp.append(r)
    else:
        print_arr.append('"' + '","'.join(temp) + '"')
        temp = []
        temp.append(r)
print_arr.append('"' + '","'.join(temp) + '"')
print("一共{}行".format(len(print_arr)))
print(",\n".join(print_arr))