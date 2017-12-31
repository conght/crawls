# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei']

from datetime import datetime

import matplotlib.dates as mdates

def drawR():
    plt.figure(figsize=(9, 20))
    plt.text(1,22200,'class 1 : > 180',color='lightcoral',ha='left')
    plt.text(1,21200,'class 2 : <= 180',color='blue',ha='left')
    plt.text(1,20200,'class 3 : <= 90',color='darkorange',ha='left')
    plt.text(1,19200,'class 4 : <= 30',color='green',ha='left')
    plt.text(1,18200,'class 5 : <= 10',color='gold',ha='left')
    n = 5
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [2287,4869,4154,1957,22133]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('R distribution')
    plt.ylabel('Numbers of the user sets')
    plt.xlabel('Classes of R')
    plt.ylim(1000, +23000)
    plt.show()

def drawF():
    plt.figure(figsize=(9, 20))
    plt.text(2,22200,'class 1 : > 6000',color='lightcoral',ha='left')
    plt.text(2,21200,'class 2 : <= 6000',color='blue',ha='left')
    plt.text(2,20200,'class 3 : <= 4500',color='darkorange',ha='left')
    plt.text(2,19200,'class 4 : <= 3000',color='green',ha='left')
    plt.text(2,18200,'class 5 : <= 1500',color='gold',ha='left')
    n = 5
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [20681,107,480,1753,12379]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('F distribution')
    plt.ylabel('Numbers of the user sets')
    plt.xlabel('Classes of F')
    plt.ylim(0, +23000)
    plt.show()

def drawT():
    plt.figure(figsize=(9, 20))
    plt.text(2,22200,'class 1 : < 15',color='lightcoral',ha='left')
    plt.text(2,21200,'class 2 : <= 30',color='blue',ha='left')
    plt.text(2,20200,'class 3 : <= 50',color='darkorange',ha='left')
    plt.text(2,19200,'class 4 : <= 80',color='green',ha='left')
    plt.text(2,18200,'class 5 : > 80',color='gold',ha='left')
    n = 5
    X = np.arange(n) + 1
    # X是1,2,3,4,5,6,7,8,柱的个数
    Y1 = [22227,2218,3074,3173,4708]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('T distribution')
    plt.ylabel('Numbers of the user sets')
    plt.xlabel('Classes of T')
    plt.ylim(1000, +23000)
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
    Y1 = [7562,13399,1750,4808,68,239,1930,5644]#np.random.uniform(0.5, 1.0, n)

    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.bar(X, Y1, width=0.35, facecolor='lightskyblue', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')
    plt.title('RFT distribution')
    plt.ylabel('Numbers of the user sets')
    plt.xlabel('Classes of RFT')
    plt.ylim(0, +15000)
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
    ,"2005-12","2006-02","2006-03"]
    Y = [22, 8, 2, 2, 10, 4, 6, 1, 2, 1, 2, 1, 1, 2,1,1,2,1,5,6,1,3,1,1,9]
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
    xs = [datetime.strptime(d, '%Y-%m').date() for d in X]
    #ys = range(len(xs))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())

    plt.figure(figsize=(len(Y), 20)) 
    #Y2 = np.random.uniform(0.5, 1.0, n)
    plt.plot(xs, Y, color='lightskyblue', label='Numbers of the register')
    plt.title('精华帖点击数分布')
    plt.ylabel('点击数（十万）')
    plt.xlabel('年份')
    plt.ylim(0, max(Y)+200)
    plt.show()

drawUser()
