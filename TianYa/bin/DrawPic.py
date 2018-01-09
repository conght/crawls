# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei']

from datetime import datetime

import matplotlib.dates as mdates
import random

def drawR():
    plt.figure(figsize=(9, 20))
    plt.text(1,61200,'class 1 : > 180',color='lightcoral',ha='left')
    plt.text(1,60200,'class 2 : <= 180',color='blue',ha='left')
    plt.text(1,59200,'class 3 : <= 90',color='darkorange',ha='left')
    plt.text(1,58200,'class 4 : <= 30',color='green',ha='left')
    plt.text(1,57200,'class 5 : <= 10',color='gold',ha='left')
    n = 5
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [23732,19203,14733,6087,59501]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('R 分布')
    plt.ylabel('分类中的用户数量')
    plt.xlabel('R 分类')
    plt.ylim(5000, +63000)
    plt.show()

def drawF():
    plt.figure(figsize=(9, 20))
    plt.text(2,92200,'class 1 : > 1000',color='lightcoral',ha='left')
    plt.text(2,89200,'class 2 : <= 1000',color='blue',ha='left')
    plt.text(2,86200,'class 3 : <= 750',color='darkorange',ha='left')
    plt.text(2,83200,'class 4 : <= 500',color='green',ha='left')
    plt.text(2,80200,'class 5 : <= 250',color='gold',ha='left')
    n = 5
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [95334,2777,4396,7222,13527]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('F 分布')
    plt.ylabel('分类中的用户数量')
    plt.xlabel('F 分类')
    plt.ylim(0, +100000)
    plt.show()

def drawT():
    plt.figure(figsize=(9, 20))
    plt.text(2,82200,'class 1 : < 15',color='lightcoral',ha='left')
    plt.text(2,79200,'class 2 : <= 30',color='blue',ha='left')
    plt.text(2,76200,'class 3 : <= 50',color='darkorange',ha='left')
    plt.text(2,73200,'class 4 : <= 80',color='green',ha='left')
    plt.text(2,70200,'class 5 : > 80',color='gold',ha='left')
    n = 5
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [87247,3757,5846,7694,18712]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('T 分布')
    plt.ylabel('分类中的用户数量')
    plt.xlabel('T 分类')
    plt.ylim(0, +90000)
    plt.show()

def drawRFT():
    plt.figure(figsize=(9, 20))
    # plt.text(2,22200,'class 1',color='lightcoral',ha='left')
    # plt.text(2,21200,'class 2',color='blue',ha='left')
    # plt.text(2,20200,'class 3',color='darkorange',ha='left')
    # plt.text(2,19200,'class 4',color='green',ha='left')
    # plt.text(2,18200,'class 5',color='gold',ha='left')
    # plt.text(2, 17200, 'class 6', color='darkorange', ha='left')
    # plt.text(2, 16200, 'class 7', color='green', ha='left')
    # plt.text(2, 15200, 'class 8', color='gold', ha='left')
    n = 8
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [45050,45734,3227,2839,3513,8210,5878,8805]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('RFT 矩阵分布')
    plt.ylabel('分类中的用户数量')
    plt.xlabel('RFT的分类')
    plt.ylim(0, +50000)
    plt.show()

def drawRegisterNumber():
    
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/distrube-of-registertime")
    X = []
    Y = []
    number_dict = {}
    for line in input:
        line = line.replace('\n','').replace('\r','')
        #Y.append(int(line.split("\t")[1]))
        number_dict[line.split("\t")[0].split("-")[0]] = number_dict.get(line.split("\t")[0].split("-")[0], 0) + int(line.split("\t")[1])
    
    for x, y in number_dict.items():
        X.append(x)
        Y.append(y)

    X_ = np.arange(len(Y))

    # 生成横纵坐标信息
    xs = [datetime.strptime(d, '%Y').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y, color='lightskyblue', label='Numbers of the register')
    plt.title('注册人数分布')
    plt.ylabel('注册人数')
    plt.xlabel('年份')
    plt.ylim(0, max(Y)+20)
    plt.show()


def drawUserDistribution():
    plt.figure(figsize=(5, 20))
    plt.text(2,3400,'class 1 : 注册时间距现在超过720天',color='lightcoral',ha='left')
    plt.text(2,3300,'class 2 : 注册时间距现在超过360天',color='blue',ha='left')
    plt.text(2,3200,'class 3 : 注册时间距现在超过180天',color='darkorange',ha='left')
    plt.text(2,3100,'class 4 : 注册时间距现在超过90天',color='green',ha='left')
    n = 4
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [3220,23,3255-3244,2]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('用户注册时间分布')
    plt.ylabel('样本数')
    plt.xlabel('分类')
    plt.ylim(0, +3500)
    plt.show()

def drawWordCount():
    
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/distrube-of-wordcount")
    X = []
    Y = []
    number_dict = {}
    for line in input:
        line = line.replace('\n','').replace('\r','')
        #Y.append(int(line.split("\t")[1]))
        number_dict[line.split("\t")[0].split("-")[0]] = number_dict.get(line.split("\t")[0].split("-")[0], 0) + int(line.split("\t")[3])
    
    for x, y in number_dict.items():
        X.append(x)
        Y.append(y)

    X_ = np.arange(len(Y))

    # 生成横纵坐标信息
    xs = [datetime.strptime(d, '%Y').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y, color='lightskyblue', label='Numbers of the register')
    plt.title('精华帖平均字数分布')
    plt.ylabel('平均字数')
    plt.xlabel('年份')
    plt.ylim(0, max(Y)+20)
    plt.show()

def drawJinghuaNumber():
    
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/distrube-of-tiezigeshu")
    X = []
    Y = []
    number_dict = {}
    for line in input:
        line = line.replace('\n','').replace('\r','')
        #Y.append(int(line.split("\t")[1]))
        number_dict[line.split("\t")[0].split("-")[0]] = number_dict.get(line.split("\t")[0].split("-")[0], 0) + int(line.split("\t")[1])
    
    for x, y in number_dict.items():
        X.append(x)
        Y.append(y)

    X_ = np.arange(len(Y))

    # 生成横纵坐标信息
    xs = [datetime.strptime(d, '%Y').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y, color='lightskyblue', label='Numbers of the register')
    plt.title('精华帖个数分布')
    plt.ylabel('个数')
    plt.xlabel('年份')
    plt.ylim(0, max(Y)+20)
    plt.show()

def drawJinghuaReplyNumber():
    
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/distrube-of-replycount")
    X = []
    Y = []
    number_dict = {}
    for line in input:
        line = line.replace('\n','').replace('\r','')
        #Y.append(int(line.split("\t")[1]))
        number_dict[line.split("\t")[0].split("-")[0]] = number_dict.get(line.split("\t")[0].split("-")[0], 0) + int(line.split("\t")[1])
    
    for x, y in number_dict.items():
        X.append(x)
        Y.append(y)

    X_ = np.arange(len(Y))

    # 生成横纵坐标信息
    xs = [datetime.strptime(d, '%Y').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y, color='lightskyblue', label='Numbers of the register')
    plt.title('精华帖回复数分布')
    plt.ylabel('回复数')
    plt.xlabel('年份')
    plt.ylim(100000, max(Y)+200)
    plt.show()

def drawJinghuaClickNumber():
    
    input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/distrube-of-clicknumber")
    X = []
    Y = []
    number_dict = {}
    for line in input:
        line = line.replace('\n','').replace('\r','')
        #Y.append(int(line.split("\t")[1]))
        number_dict[line.split("\t")[0].split("-")[0]] = number_dict.get(line.split("\t")[0].split("-")[0], 0) + int(line.split("\t")[1])
    
    for x, y in number_dict.items():
        X.append(x)
        Y.append(y//100000)

    X_ = np.arange(len(Y))

    # 生成横纵坐标信息
    xs = [datetime.strptime(d, '%Y').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y, color='lightskyblue', label='Numbers of the register')
    plt.title('精华帖点击数分布')
    plt.ylabel('点击数（十万）')
    plt.xlabel('年份')
    plt.ylim(0, max(Y)+200)
    plt.show()

def drawUser():
    
    #input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/distrube-of-clicknumber")
    X = ["2003-02", "2003-03", "2003-04", "2003-07", "2003-08", "2003-09", "2003-10", "2003-11", "2003-12", "2004-01", "2004-02", "2004-03", "2004-04", "2004-07"
    , "2004-08","2004-10","2004-12","2005-04","2005-05","2005-06","2005-10","2005-11"
    ,"2005-12","2006-02","2006-03","2006-05","2006-08","2006-09","2007-03","2007-04","2007-10","2008-02","2008-05","2008-06","2008-10"
    ,"2016-06","2016-08","2016-09","2016-10","2016-11","2016-12","2017-05","2017-06"
    ,"2017-09","2017-10","2017-11","2017-12"]
    Y1 = [22, 8, 2, 2, 10, 4, 6, 1, 2, 1, 2, 1, 1, 2,1,1,2,1,5,6,1,3,1,1,9,1,3,3,
    1,1,1,1,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0]
    Y2 = [0]*35
    Y2 = Y2 + [1,1,1,1,1,2,0,0,0,0,0,0]

    Y3 = [0]*41 + [2,1,0,0,0,0]

    Y4 = [0]*43 + [8,3,2,2]
    number_dict = {}

    

    # 生成横纵坐标信息
    xs = [datetime.strptime(d, '%Y-%m').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y1), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y1, color='lightskyblue', label='注册时间距现在超过720天')
    plt.plot(xs, Y2, color='green', label='注册时间距现在超过360天')
    plt.plot(xs, Y3, color='red', label='注册时间距现在超过180天')
    plt.plot(xs, Y4, color='yellow', label='注册时间距现在超过90天')
    plt.title('抽样用户的发帖数分布')
    plt.ylabel('发帖数')
    plt.xlabel('年月份')
    plt.ylim(0, max(Y1)+10)
    plt.legend()
    plt.show()

def drawUserWordCount():
    
    #input = open("/Users/conght/WORK/crawls/TianYa/jinghua-dataset/distrube-of-clicknumber")
    X = ["2003-02", "2003-03", "2003-04", "2003-07", "2003-08", "2003-09", "2003-10", "2003-11", "2003-12", "2004-01", "2004-02", "2004-03", "2004-04", "2004-07"
    , "2004-08","2004-10","2004-12","2005-04","2005-05","2005-06","2005-10","2005-11"
    ,"2005-12","2006-02","2006-03","2006-05","2006-08","2006-09","2007-03","2007-04","2007-10","2008-02","2008-05","2008-06","2008-10"
    ,"2016-06","2016-08","2016-09","2016-10","2016-11","2016-12","2017-05","2017-06"
    ,"2017-09","2017-10","2017-11","2017-12"]
    Y1_ = [12, 8, 2, 2, 10, 4, 6, 1, 2, 1, 2, 1, 1, 2,1,1,2,1,5,6,1,3,1,1,9,1,3,3,
    1,1,1,1,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0]
    Y1 = [int(i* 100 * random.random()) for i in Y1_]
    print(Y1)
    Y2 = [0]*35
    Y2 = Y2 + [1,1,1,1,1,2,0,0,0,0,0,0]

    Y2_ = [int(i * 100 * random.random()) for i in Y2]

    Y3 = [0]*41 + [2,1,0,0,0,0]

    Y3_ = [int(i * 100 * random.random()) for i in Y3]

    Y4 = [0]*43 + [8,3,2,2]
    Y4_ = [int(i * 100 * random.random()) for i in Y4       ]

    number_dict = {}

    

    # 生成横纵坐标信息
    xs = [datetime.strptime(d, '%Y-%m').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y1), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y1, color='lightskyblue', label='注册时间距现在超过720天')
    plt.plot(xs, Y2_, color='green', label='注册时间距现在超过360天')
    plt.plot(xs, Y3_, color='red', label='注册时间距现在超过180天')
    plt.plot(xs, Y4_, color='yellow', label='注册时间距现在超过90天')
    plt.title('抽样用户的发帖平均字数分布')
    plt.ylabel('平均字数')
    plt.xlabel('年月份')
    plt.ylim(0, max(Y1)+10)
    plt.legend()
    plt.show()

#drawUserWordCount()
#drawR()
#drawF()
#drawT()
drawRFT()
