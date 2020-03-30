# -*- coding:utf-8 -*-
"""
@Author  : zhclwr
从 swagger直接复制接口放到 swagger_to_api.txt 文件
格式参照 swagger_to_api.txt 文件
运行本脚本即可
"""
res = {
    'GET': '''// {}
export async function {}(payload: any){{
	let res = await ajax.get("{}", {{params:payload}})
	return res.data.result
}}
''',
    'POST': '''// {}
export async function {}(payload: any){{
	let res = await ajax.post('{}', payload)
	return res.data.result
}}
''',
    'PUT': '''// {}
export async function {}(payload: any){{
	let res = await ajax.put('{}', payload)
	return res.data.result
}}
''',
    'DELETE': '''// {}
export async function {}(payload: any){{
	let res = await ajax.delete('{}', {{params:payload}})
	return res.data.result
}}
'''
}

index = 0  # 当前位置
fun_type = ''  # 方法类型
comment = ''  # 注释
fun = ''  # 方法名
fun_ = ''  # 整个方法体

with open('swagger_to_api.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        pos = index % 3
        if pos == 0:
            fun_type = line.replace('\n', '')
        elif pos == 1:
            fun_ = line.replace('\n', '')
            fun_arr = fun_.split('/')
            fun = fun_arr[len(fun_arr) - 1]
        else:
            comment = line.replace('\n', '')
            print(res.get(fun_type).format(comment, fun, fun_))
        index += 1
