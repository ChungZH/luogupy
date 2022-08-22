import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63', 'x-luogu-type': 'content-only'}

res = requests.get('https://www.luogu.com.cn/problem/P8486', headers=headers)
txt = res.text.replace('\\', '\\\\')
content = txt.encode('utf-8').decode('unicode-escape')

contentjson = json.loads(content, strict=False)
currentData = contentjson["currentData"]["problem"]

difficulties = ['入门', '普及-', '普及/提高-', '普及+/提高',
                '提高+/省选-', '省选/NOI-', 'NOI/NOI+/CTSC']

pid = currentData["pid"]
title = currentData["title"]
difficulty = currentData["difficulty"]-1
background = currentData["background"]
description = currentData["description"]
inputFormat = currentData["inputFormat"]
outputFormat = currentData["outputFormat"]
# translation = currentData["translation"]
hint = currentData["hint"]

print('「', pid, title, '」', difficulties[difficulty], end="\n\n")
if background != '':
    print("题目背景", background, sep="\n")
print("题目描述", description, sep="\n")
print("输入格式", inputFormat, sep="\n")
print("输出格式", outputFormat, sep="\n")
# if translation!='':
#    print("题意翻译", translation, sep="\n")
print("输入输出样例")
for index, i in enumerate(currentData["samples"]):
    print("输入 #{0}".format(index+1), i[0], sep="\n")
    print("输出 #{0}".format(index+1), i[1], sep="\n")
print("\n")
print("说明/提示", hint, sep="\n")

# print(currentData)
