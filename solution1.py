# -- coding: utf-8 --
"""
Created on Fri Feb 21 02:08:07 2020

@author: 18moh
"""

import copy

f = open("b_read_on.txt", "r")
l=f.read().split('\n')

for i in range(len(l)):
    l[i]=l[i].split()

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]=int(l[i][j])

det=l[0]
book=l[1]


del l[0]
del l[0]

while(l[-1]==[]):
    del l[-1]

lib=[]

while(len(l)>0):
    lib.append([l[0],l[1]])
    del l[0:2]

score=0
pick=[]
index=[]
ready=0

def nextpick(pick,lib):
    mini=10000000
    ind=0
    for i in range(len(lib)):
        if(lib[i][0][1]<mini and (lib[i] not in pick)):
            ind=i
            mini=lib[i][0][1]
    return ind
            
for i in range(det[2]-1):
    if(ready<=0 and len(pick)<len(lib)):
        index.append(nextpick(pick,lib))
        pick.append(lib[nextpick(pick,lib)])
        ready=pick[-1][0][1]
        
    m=len(pick)
    if(ready>0):
        m-=1
    for j in range(m):
        k=pick[j][0][2]
        while(k>0):
            if(len(pick[j][1])>0):
                del pick[j][1][-1]
            k-=1
    ready-=1
    
f = open("a_example.txt", "r")
l=f.read().split('\n')

for i in range(len(l)):
    l[i]=l[i].split()

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]=int(l[i][j])

det=l[0]
book=l[1]


del l[0]
del l[0]

while(l[-1]==[]):
    del l[-1]

lib=[]

while(len(l)>0):
    lib.append([l[0],l[1]])
    del l[0:2]
 

number=len(index)
form=[]

for i in range(len(index)):
    libid=index[i]
    scanned=len(lib[index[i]][1])-len(pick[i][1])
    books=[]
    for x in lib[index[i]][1]:
        if(x not in pick[i][1]):
            books.append(x)
    form.append([[libid,scanned],books])


f = open("sol2.txt", "w")
f.write(str(number))
for x in form:
    f.write('\n')
    f.write(str(x[0][0]))
    f.write(' ')
    f.write(str(x[0][1]))
    f.write('\n')
    for y in x[1]:
        f.write(str(y))
        f.write(' ')
    
f.close()