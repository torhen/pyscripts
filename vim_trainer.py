import os, random

quote="""Who the fuck is Alice?"""

def task_00(quote):
    question = 'toggle between beginning and end (gg), (G)'
    return f'\n{question}\n'

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
    question = 'replace delete letters (x)'
    res = quote
    res = res.replace('e', 'e-')
    res = res.replace('a', 'a-')
    res = res.replace('r', 'r-')
    res = res.replace('t', 't-')
    return f'\n{question}\n{res}\n'

def task_04(quote):
    question = 'delete words (dw)'
    res = quote
    res = res.replace(' ', ' xxxxxx ')
    return f'\n{question}\n{res}\n'

def task_05(quote):
    question = 'join the lines (J)'
    l = quote.split()
    res = '\n'.join(l)
    return f'\n{question}\n{res}\n'

def task_06(quote):
    question = 'delete lines (dd)'
    return f'\n{question}\n{quote}\n{quote}\n{quote}\n{quote}\n'

def task_07(quote):
    question = 'duplicat lines (yy), (p)'
    return f'\n{question}\n{quote}\n'

def task_08(quote):
    question = 'order the word (dw) (p)'
    l = quote.split()
    random.shuffle(l)
    res = ' '.join(l)
    return f'\n{question}\n"{res} "\n'

def task_09(quote):
    question = 'order the lines (dd) (p)\n'
    l = quote.split()
    random.shuffle(l)
    res = '\n'.join(l)
    return f'\n{question}\n{res}\n'

tasks = []
tasks.append(task_00)
tasks.append(task_01)
tasks.append(task_02)
tasks.append(task_03)
tasks.append(task_04)
tasks.append(task_05)
tasks.append(task_06)
tasks.append(task_07)
tasks.append(task_08)
tasks.append(task_09)

random.shuffle(tasks)

txt = f'quote: {quote}\n'

for task in tasks:
    txt = txt + task(quote)

with open('test.txt', 'w') as fin:
            fin.write(txt)

os.system('vim test.txt')
os.remove('test.txt')

