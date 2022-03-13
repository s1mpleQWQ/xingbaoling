import os
import sys


filename = sys.argv[1]
filepath = os.path.abspath(filename)
print(filepath)
txt = []
with open(filepath, "r", encoding='ANSI') as f:
    for line in f.readlines():
        data = line.splitlines()
        for cont in data:
            sub_cont = cont.split()
        if sub_cont:
            txt.append(sub_cont)
x = len(txt)
y = 3

with open('yq_out.txt', "a", encoding='ANSI') as file:
    a = 0
    b = []
    z = []

    for i in range(0, x):
        if a == 0:
            b = txt[i][0]
            file.write(txt[i][0]+'\n'+txt[i][1]+' '+txt[i][2])
            a = a+1
        if a != 0:
            z = txt[i][0]
            if z != b:
                a = 1
                file.write('\n'+txt[i][0] + '\n' + txt[i][1] + ' ' + txt[i][2])
                b = txt[i][0]
            if z == b:
                file.write('\n'+txt[i][1] + ' ' + txt[i][2])
