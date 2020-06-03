str = `"recordDate": new Date(),
"userId": 0,
"userName": "",
"shiftName": "",
"cc": 0,
"warShips": 0,
"changeMed": 0,
"drawBlood": 0,
"bloodGlucose": 0,
"grave": 0,
"offTubeSeal": 0,
"sg": 0,
"eleMonitor": 0,
"oxygen": 0,
"emergy": 0,
"wgstx": 0,
"njmfg": 0,
"wb": 0,
"njmbr": 0,
"ndcc": 0,
"bb": 0,
"crrt": 0,
"zk": 0,
"xhzxj": 0,
"remarks": "",`
let arr = str.split('\n')
arr.forEach(element => {
    let elementArr = element.split(':')
    let key = elementArr[0].replace('"', '').replace('"', '')
    console.log(`${key}: [{required: true, message: '请输入内容'}],`)
});