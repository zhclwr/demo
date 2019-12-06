resArr = []
with open('fileSelect.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line)
        arr = line.split()
        resArr.append(arr)
for res in resArr:
    print('<Option value="{}">{}</Option>'.format(res[0], res[1]))