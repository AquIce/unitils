import re

datas = ''

with open('datas.unity', 'r') as f:
    datas = f.read()

lst = ['Front', 'Back', 'Right', 'Left', 'Up', 'Down']

datas = datas.split('---')

ids = {}

for i in lst:
    for j in datas:
        if i + '_Controls' in j:
            ids[i] = j.split('- component: {fileID: ')[1].split('}\n')[0]

lst.append('Clockwise')
lst.append('Counterclockwise')

for i in ids.keys():
    for j in range(len(datas)):
        if 'm_Father: {fileID: ' + ids[i] + '}' in datas[j]:
            for k in lst:
                datas[j - 1] = re.sub(f'm_Name: (Front|Back|Right|Left|Up|Down)_{k}Arrow', f'm_Name: {i}_{k}Arrow', datas[j - 1])

with open('datas.unity', 'w') as f:
    f.write('---'.join(datas))