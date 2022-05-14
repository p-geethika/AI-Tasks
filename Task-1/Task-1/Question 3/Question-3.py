#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question - 3
fh=open("about.txt","r")
r=fh.read()
rs=r.split(' ')
d={}
l=[]
count=0
c=''
for j in range(len(rs)):
    for char in rs[j]:
        if char.isalpha():
            c=c+char
        else:
            continue
    rs[j]=c
    c=''


for i in range(len(rs)):
    if len(rs[i])>=6:
        l.append(rs[i])
    if rs[i] not in d:
        d[rs[i]]=count
    if rs[i] in d:
        d[rs[i]]+=1

list_6=[]
for i in l:
    if i not in list_6:
        list_6.append(i)

print("Words with atleast 6 letters")  
print()      
for i in list_6:
    print(i)
    
freq=0
keys=''
for i in d:
    if d[i]>freq:
        freq=d[i]
        keys=i

print()        
print("The most frequent word:",keys)


# In[ ]:




