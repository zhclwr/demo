// swagger 出参生成表格
a = `patientName	string
患者姓名

vaType	string
通路类型

bloodVelocity	integer($int32)
血流量

dryWeight	number($double)
干体重

radio	string
血流量/干体重

dialysateFlowRate	integer($int32)
透析液流量

dialyzer	string
透析器

totalTimes	string
透析总时间

count	integer($int32)
透析次数`


title = ''
key = ''
print = console.log
arr = a.split('\n')
for(let i in arr){
    if (i % 3 === 0) {
        key = arr[i].split('\t')[0]
    } else if (i % 3 === 1) {
        title = arr[i]
        print(`{
    title: '${title}',
    key: '${key}'
},`)
    }
}