from math import log
from collections import Counter
import json

class DT:

    def __init__(self, data):
        ctr = Counter([r[8] for r in data])
        default = ctr.most_common(1)[0][0]  #fml

        if ctr.most_common()[0][1] == len(data)/2:
            default = 'yes'

        self.tree = self.gen_dt(data, {i for i in range(8)}, default)


    def gen_dt(self, data, attrs, default):

        # majority class of parent
        if len(data) == 0:
            return default

        # all elements of the same class
        classes = [r[8] for r in data]
        if all(map(lambda x: x == 'yes', classes)):
            return 'yes'
        if all(map(lambda x: x == 'no', classes)):
            return 'no'

        # calculate majority
        ctr = Counter(classes)
        maj = ctr.most_common(1)[0][0]
        if ctr.most_common()[0][1] == len(data)/2:
            maj = 'yes'

        # no more attributes to clasify - return majority
        if len(attrs) == 0:
            return maj

        best = self.choose_attr(data, attrs)
        root = [best, {}]
        for v in ('low','medium','high', 'very high'):

            # partition data on the nominal value of best attribute
            attr_partition = [r for r in data if r[best] == v]
            attr_subtree = self.gen_dt(attr_partition, attrs.difference({best}), maj)
            root[1][v] = attr_subtree

        return root

    def choose_attr(self, data, attrs):
        parent_ent = self.get_ent(data)
        gains = []
        for a in attrs:
            attr_ent = 0
            for v in ('low','medium','high','very high'):
                part = [r for r in data if r[a] == v]
                attr_ent += len(part)/len(data)*self.get_ent(part)
            gains.append((parent_ent - attr_ent, a))
        return max(gains)[1]

    def get_ent(self, data):
        if len(data) == 0:
            return 0

        yes = len([r for r in data if r[8] == 'yes'])/len(data)
        no = len([r for r in data if r[8] == 'no'])/len(data)
        if 1 in (yes, no):
            return 0

        return -yes*log(yes,2)-no*log(no,2)

    def classify(self, row):
        root = self.tree
        attr = None
        print(json.dumps(root))
        while True:
            attr = root[0]
            if attr in ('y', 'n'):
                break

            val = row[attr]
            root = root[1][val]

        return attr == 'y'

