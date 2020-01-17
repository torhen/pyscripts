import os
quote="""Who the fuck is Alice?"""

def exam_01(quote):
    res =quote
    for c in ['a', 'e', 'i', 'o', 'u']:
        res = res.replace(c, '_')
    with open('test.txt', 'w') as fin:
            fin.write(res)
exam_01(quote)
os.system('vim test.txt')

