const a = `RecordId	执行记录id
AfterMemo	治疗前情况
BeforeMemo	治疗后反应
PatientId	病人唯一id
PatientName	病人姓名
ExecTime	执行时间`
const arr = a.split('\n')
print = console.log
print(arr)
arr.forEach(item => {
    let lineArr = item.split('\t')
    print(`{
        title: '${lineArr[1]}',
        key: '${lineArr[0]}',
        width: 150
    },`)
})