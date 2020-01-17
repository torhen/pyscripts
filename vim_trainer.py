import os
quote="""Who the fuck is Alice?"""

def exam_01(quote):
    task = 'replace letters (r)'
    res =quote
    for c in ['a', 'e', 'i', 'o', 'u']:
        res = res.replace(c, '_')
    return f'{task}\n{res}'

txt = f'quote: {quote}\n\n'
txt = txt + exam_01(quote)

with open('test.txt', 'w') as fin:
            fin.write(txt)
os.system('vim test.txt')

