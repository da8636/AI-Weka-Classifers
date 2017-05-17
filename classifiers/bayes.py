import numpy as np
from .utils import norm

class Bayes:

    def __init__(self,data):
        self.dist_data = self.get_dist_data(data)

    def get_dist_data(self, data):
        yes = []
        no = []

        # partition data into classes
        for r in data:
            if r[-1] == 'yes':
                yes.append(r[:-1])
            else:
                no.append(r[:-1])

        self.p_yes = len(yes)/len(data)
        self.p_no = len(no)/len(data)

        yes = np.array(yes)
        no = np.array(no)

        dist_data = []
        for c in range(8):
            yes_m = np.mean(yes[:,c])
            yes_std = np.std(yes[:,c])
            no_m = np.mean(no[:,c])
            no_std = np.std(no[:,c])

            dist_data.append([(yes_m, yes_std),(no_m,no_std)])

        return dist_data

    def classify(self, row):
        yes = self.p_yes
        no = self.p_no

        for c in range(8):
            yes *= norm(row[c], self.dist_data[c][0][0], self.dist_data[c][0][1])
            no *= norm(row[c], self.dist_data[c][1][0], self.dist_data[c][1][1])

        return yes >= no
