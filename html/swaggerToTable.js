// swagger 出参生成表格
a = `dialysisWay	string
透析模式

creationTime	string($date-time)
创建时间

creatorUserId	integer($int64)
创建人编号

creatorUser	string
创建人姓名

id	integer($int32)
主键Id

remarks	string
备注
`


title = ''
key = ''
print = console.log
arr = a.split('\n')
for(let i in arr){
    if (i % 3 === 0) {
        key = arr[i].split('\t')[0]
    } else if (i % 3 === 1) {
        title = arr[i].replace('[必填]', '')
        print(`{
    title: '${title}',
    key: '${key}'
},`)
    }
}