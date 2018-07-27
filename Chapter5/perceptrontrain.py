#coding: utf-8
# training_set 数据集{x,lable}，激活函数 f = sum(w*x) + b
# 训练过程：f大于0表示real_lable=1，f小于0表示real_label=-1。不断调整参数{w,b}，直到real_label符合expected_label
import os

# An example in that book, the training set and parameters' sizes are fixed
training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1]]     # 线性可分数据集
#training_set = [[(3, 3), -1], [(1, 3), 1], [(3, 1), 1], [(1, 1), -1]]  # 非线性数据集（异或）

w = [0, 0]
b = 0

# update parameters using stochastic gradient descent
def update(item):
    global w, b
    w[0] = w[0] + 1 * item[1] * item[0][0] # 1 表示学习率
    w[1] = w[1] + 1 * item[1] * item[0][1]
    b = b + 1 * item[1]
    # print w, b # you can uncomment this line to check the process of stochastic gradient descent

# calculate the functional distance between 'item' an the dicision surface
def cal(item):
    global w, b
    res = 0
    for i in range(len(item[0])):   # res = sum(x*w)
        res += item[0][i] * w[i]
    res += b                        # res = sum(x*w) + b
    res *= item[1]                  # res = (sum(x*w) + b) * lable
    return res

# check if the hyperplane can classify the examples correctly
def check():
    flag = False
    for item in training_set:   # 对所有数据集完成一次训练
        if cal(item) <= 0:
            flag = True
            update(item)
    if not flag:
        print "RESULT: w: " + str(w) + " b: "+ str(b)
        os._exit(0)

if __name__=="__main__":
    for i in range(1000):   # epoch = 1000
        check()
    print "The training_set is not linear separable. "
