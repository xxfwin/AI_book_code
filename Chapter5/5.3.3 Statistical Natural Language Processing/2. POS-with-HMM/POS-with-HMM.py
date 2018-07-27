# -*- coding: UTF-8 -*-
# 打开一个文件
# coding:utf-8


import sys

reload(sys)
sys.setdefaultencoding('utf8')
import codecs
import re
import math
from operator import itemgetter, attrgetter

# 所有词语
ww = []
# 所有的词性
pos = []
# 每个词性出现的频率
fre = {}
# 先验概率矩阵
pi = {}
# 状态转移概率矩阵
A = {}
# 观测概率矩阵
B = {}
# dp概率
dp = []
# 路径记录
pre = []

zz = {}

fin = codecs.open("处理语料.txt", "r", "utf-8")
while (True):
    text = fin.readline()
    if (text == ""):
        break
    tmp = text.split(" ")
    n = len(tmp)
    for i in range(0, n - 1):
        word = tmp[i].split('/')
        if (word[1] not in pos):
            pos.append(word[1])
fin = codecs.open("分词语料.txt", "r", "utf-8")
text = fin.read()
ww = text.split("\n")

n=len(pos)
#初始化概率矩阵
for i in pos:
    pi[i]=0
    fre[i]=0
    A[i]={}
    B[i]={}
    for j in pos:
        A[i][j]=0
    for j in ww:
        B[i][j]=0

#计算概率矩阵
line=0#总行数
fin=codecs.open("处理语料.txt","r","utf-8")
while(True):
    text=fin.readline()
    if(text=="\n"):
        continue
    if(text==""):
        break
    tmp=text.split(" ")
    n=len(tmp)
    line+=1
    for i in range(0,n-1):
        word=tmp[i].split('/')
        pre=tmp[i-1].split('/')
        fre[word[1]]+=1
        if(i==1):
            pi[word[1]]+=1
        elif(i > 0):
            A[pre[1]][word[1]]+=1
        B[word[1]][word[0]]+=1

cx={}
cy={}
for i in pos:
    cx[i]=0
    cy[i]=0
    pi[i]=pi[i]*1.0/line
    for j in pos:
        if(A[i][j]==0):
            cx[i]+=1
            A[i][j]=0.5
    for j in ww:
        if(B[i][j]==0):
            cy[i]+=1
            B[i][j]=0.5

for i in pos:
    pi[i]=pi[i]*1.0/line
    for j in pos:
        A[i][j]=A[i][j]*1.0/(fre[i]+cx[i])
    for j in ww:
        B[i][j]=B[i][j]*1.0/(fre[i]+cy[i])

print "训练结束"

while(True):
    tmp=raw_input("请输入需要词性标注的句子，以空格分割: ")
    if(tmp=="-1"):
        break
    text=tmp.split(" ")

    num=len(text)
    for i in range(0,num):
        text[i]=unicode(text[i])
    dp=[{} for i in range(0,num)]
    pre=[{} for i in range(0,num)]
    #初始化概率
    for k in pos:
        for j in range(0,num):
            dp[j][k]=0
            pre[j][k]=""
    n=len(pos)
    for c in pos:
        if(B[c].has_key(text[0])):
            dp[0][c]=pi[c]*B[c][text[0]]*1000
        else:
            dp[0][c]=pi[c]*0.5*1000/(cy[c]+fre[c])
    for i in range(1,num):
        for j in pos:
            for k in pos:
                tt=0
                if(B[j].has_key(text[i])):
                    tt=B[j][text[i]]*1000
                else:
                    tt=0.5*1000/(cy[j]+fre[j])
                if(dp[i][j]<dp[i-1][k]*A[k][j]*tt):
                    dp[i][j]=dp[i-1][k]*A[k][j]*tt
                    pre[i][j]=k
    res={}
    MAX=""
    for j in pos:
        if(MAX=="" or dp[num-1][j]>dp[num-1][MAX]):
            MAX=j
    if(dp[num-1][MAX]==0):
        print "您的句子超出我们的能力范围了"
        continue
    i=num-1
    while(i>=0):
        res[i]=MAX
        MAX=pre[i][MAX]
        i-=1
    for i in range(0,num):
        print text[i].decode('utf-8')+"\\"+res[i].decode('utf-8'),
    print ""