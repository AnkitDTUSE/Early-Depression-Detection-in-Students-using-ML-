import math

def accuracy(TN,FP,FN,TP):
    return (TP+TN)/(TP+TN+FP+FN)

def precision(TN,FP,FN,TP):
    return TP/(TP+FP)

def recall(TN,FP,FN,TP):
    return TP/(TP+FN)

def fmeasure(TN,FP,FN,TP):
    return (2*precision(TN,FP,FN,TP)*recall(TN,FP,FN,TP))/(precision(TN,FP,FN,TP)+recall(TN,FP,FN,TP))

def specificity(TN,FP,FN,TP):
    return (1-fmeasure(TN,FP,FN,TP))

def gmean(TN,FP,FN,TP):
    return math.sqrt(recall(TN,FP,FN,TP)*specificity(TN,FP,FN,TP))

def gmeasure(TN,FP,FN,TP):
    return math.sqrt(recall(TN,FP,FN,TP)*precision(TN,FP,FN,TP))