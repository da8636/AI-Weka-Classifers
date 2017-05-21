from classifiers import Bayes, DT
from sys import argv
import numpy as np

f = open(argv[1])
data = [l.strip().split(',') for l in f]
folds = [[]]
for r in data:
    if r[0].startswith('fold'):
        continue
    if r[0] == '':
        folds.append([])
        continue
    folds[-1].append(r)

acc = 0
for i in range(len(folds)):
    test = folds[i]
    train_folds = folds[:i] + folds[i+1:]
    training = [r for f in train_folds for r in f]

    if argv[2] == 'NB':

        training = [[float(x) for x in r[:-1]]+[r[-1]] for r in training]
        b = Bayes(training)

        bad = 0
        for l in test:
            r = [float(x) for x in l[:-1]]
            res = 'yes' if b.classify(r) else 'no'
            if res != l[-1]:
                bad += 1

        acc += 1 - bad/len(test)

    else:

        dt = DT(training)

        bad = 0
        for l in test:
            r = l[:-1]
            res = 'yes' if dt.classify(r) else 'no'
            if res != l[-1]:
                bad += 1

        acc += 1 - bad/len(test)
print("TOTAL ACCURACY: ", acc/10)
