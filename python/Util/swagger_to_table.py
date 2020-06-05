str = '''recordDate	string($date-time)
记录日期[必填]

userId	integer($int32)
护士Id[必填]

userName	string
护士姓名[必填]

shiftName	string
班次[必填]

cc	integer($int32)
穿刺[必填]

warShips	integer($int32)
穿刺[必填]

changeMed	integer($int32)
换药[必填]

drawBlood	integer($int32)
抽血[必填]

bloodGlucose	integer($int32)
血糖[必填]

grave	integer($int32)
危重[必填]

offTubeSeal	integer($int32)
下机封管

sg	integer($int32)
串灌[必填]

eleMonitor	integer($int32)
心电监护[必填]

oxygen	integer($int32)
吸氧[必填]

emergy	integer($int32)
急诊[必填]

wgstx	integer($int32)
无肝素透析[必填]

njmfg	integer($int32)
尿激酶封管[必填]

wb	integer($int32)
微泵[必填]

njmbr	integer($int32)
尿激酶泵入[必填]

ndcc	integer($int32)
难度穿刺[必填]

bb	integer($int32)
白班[必填]

crrt	integer($int32)
CRRT[必填]

zk	integer($int32)
质控[必填]

xhzxj	integer($int32)
新患者宣教[必填]'''

res = '''{{
    type: '{}',
    label: '{}',
    key: '{}',
    inputType: '{}'
}},'''
arr = str.split('\n')
index = 0
type = "input"
label = ""
key = ""
input_type = ""
for i in arr:
    pos = index % 3
    if pos == 0:
        arr = i.split('\t')
        key = arr[0]
        if 'integer' in i:
            input_type = 'number'
        else:
            input_type = ""
    elif pos == 1:
        label = i.replace('[必填]', '')
    else:
        print(res.format(type, label, key, input_type))
    index += 1