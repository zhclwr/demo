res = []
with open('test.txt', mode='r', encoding="utf-8") as f:
    for line in f:
        arr = line.split()
        print(arr)
        res.append(arr[1])
r = '\t'.join(res)
with open('res.txt', mode='w', encoding="utf-8") as f:
    # print(r)
    f.write(r)