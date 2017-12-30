# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

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


drawRFT()