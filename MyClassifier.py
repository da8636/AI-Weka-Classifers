from classifiers import Bayes, DT
from sys import argv
import numpy as np

f = open(argv[1])
data = [l.strip().split(',') for l in f]
f.close()
t_f = open(argv[2])

if argv[3] == 'NB':

    data = [[float(x) for x in r[:-1]]+[r[-1].strip()] for r in data]
    b = Bayes(data)

    for l in t_f:
        r = [float(x) for x in l.split(',')]
        if b.classify(r):
            print('yes')
        else:
            print('no')
else:

    dt = DT(data)

    for l in t_f:
        if dt.classify(l.strip().split(',')):
            print('yes')
        else:
            print('no')
