#coding:utf-8
# This code calculates the mean average precision score, for all input parameter combinations, using all outputs of the rev2 algorithm.
# This is for the unsupervised case.

from collections import defaultdict
import numpy
import sys
import os
import subprocess

network = sys.argv[1]
COUNT = 250

# load ground truth
f = open("./data/%s/%s_gt.csv" % (network, network),"r")
goodusers = set()
badusers = set()

for l in f:
        l = l.strip().split(",")
        if l[1] == "-1":
                badusers.add('u'+l[0])
        else:
                goodusers.add('u'+l[0])
f.close()
print(len(badusers), len(goodusers))

# read all the scores from running rev2code.py with different parameter combinations
scores = defaultdict(list)
fnames = os.listdir("results/")
for fname in fnames:
    if network not in fname:
        continue
    if "result" in fname: # this is the precision score; ignore
        continue
    f = open("results/%s" % fname, "r")
    for l in f:
        l = l.strip().split(",")
        if l[1] == "nan":
                continue
        if l[2] == "nan":
                continue
        scores[l[0]].append(float(l[1]))

# combine scores for each node 
uniscores = {}
for score in scores:
    uniscores[score] = numpy.mean(scores[score])

# sort all nodes based on their scores and store it
import operator
sortedlist = sorted(uniscores.items(), key= lambda x: x[1])

fw = open("results-combined/%s-mean-scores.csv" % network,"w")
for sl in sortedlist:
    fw.write("%s, %f\n" % (sl[0], float(sl[1]))) #添加float!
fw.close()

# calculate the mean average precision from all the scores
fnames = ["results-combined/%s-mean-scores.csv" % (network)]
fww = open("results-combined/%s-mean-scores-result.csv" % (network), "w")

for idx in range(len(fnames)):
    fname = fnames[idx]
    bashCommand = "wc -l %s" % fname
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    NLINES  = int(process.communicate()[0].split(" ")[0])	#print fname
    Ys = []
    Ys2 = []
    X = []
    for NUSERS in range(1,COUNT):
        i = -1
        f = open(fname,"r")

        c11 = 0
        c12 = 0
        c21 = 0
        c22 = 0
        x = 0
        for l in f:
            i +=1
            l = l.strip().split(",")
            '''if i < NUSERS:
                if l[0] in goodusers:
                    c11 += 1
                elif l[0] in badusers:
                    c12 += 1'''
            if i >= NLINES - NUSERS:
                x += 1
                if l[0] in goodusers:
                    c21 +=1
                elif l[0] in badusers:
                    c22 += 1
        f.close()
        print(c11, c12, c21, c22)
        X.append(c21+c22+1)
        Ys.append((c22)*1.0/(c21+c22)) #修改
        #X.append(c11+c12+1)
        Ys2.append((c11)*1.0/(c11+c12+1))

        #必须加float转化成浮点数才能用%f输出
        fww.write("%f, %f\n" % (float(numpy.mean(Ys)), float(numpy.mean(Ys2))))
        print ("Mean Average precision for fraud prediction = %f, for benign user prediction = %f" %(float(numpy.mean(Ys)), float(numpy.mean(Ys2))))
        fww.close()
        print (Ys2)
