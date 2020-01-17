import os, random

quote="""Who the fuck is Alice?"""

def task_01(quote):
    question = 'jump between words (w), (b)'
    return f'\n{question}\n{quote}\n'
    
def task_02(quote):
    question = 'replace letters (r)'
    res = quote
    for c in ['a', 'e', 'i', 'o', 'u']:
        res = res.replace(c, '_')
    return f'\n{question}\n{res}\n'

def task_03(quote):
    question = 'replace delete letters (x)\n'
    res = quote
    res = res.replace('e', 'e-')
    res = res.replace('a', 'a-')
    res = res.replace('r', 'r-')
    res = res.replace('t', 't-')
    return f'\n{question}\n{res}\n'

tasks = []
tasks.append(task_01)
tasks.append(task_02)
tasks.append(task_03)

random.shuffle(tasks)

txt = f'quote: {quote}\n'

for task in tasks:
    txt = txt + task(quote)

with open('test.txt', 'w') as fin:
            fin.write(txt)

os.system('vim test.txt')

