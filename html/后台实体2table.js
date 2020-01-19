a = `/// <summary>
/// 项目名称
/// </summary>
public string Name { get; set; }
/// <summary>
/// 项目类型
/// </summary>
public string ItemType { get; set; }
/// <summary>
/// 规格
/// </summary>
public string Model { get; set; }
/// <summary>
/// 超出治疗方案自付金额
/// </summary>
public string Ccje { get; set; }
/// <summary>
/// 金额
/// </summary>
public string Je { get; set; }
/// <summary>
/// 自理金额
/// </summary>
public string Zlje { get; set; }
/// <summary>
/// 自费金额
/// </summary>
public string Zfje { get; set; }
/// <summary>
/// 收费项目等级
/// </summary>
public string Level { get; set; }
/// <summary>
/// 全额自费标志
/// </summary>
public string Flag { get; set; }
/// <summary>
/// 列入医保金额
/// </summary>
public string Ybje { get; set; }`

title = ''
key = ''
print = console.log
arr = a.split('\n')
for(let i in arr){
    if (i % 4 === 1) {
        title = arr[i].split(' ')[1]
    } else if (i % 4 === 3) {
        key = arr[i].split(' ')[2].toLowerCase()
        print(`{
    title: '${title}',
    key: '${key}',
    width: 120
},`)
    }
}