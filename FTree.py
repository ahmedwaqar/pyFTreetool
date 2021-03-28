from abc import ABC
import math


class AbstractGates(ABC):
    def and_gate(self):
        pass

    def or_gate(self):
        pass


class Gates(AbstractGates):
    def __init__(self):
        pass

    def atom_extend(self, lnodes, rnodes):
        out = [x[:] for x in rnodes]
        for i in out:
            i.extend(lnodes)
        return out

    def and_gate(self, lnodes, rnodes):
        out = []
        for i in lnodes:
            out += self.atom_extend(i, rnodes)
        return out


    def or_gate(self, lnodes, rnodes):
        out = [x[:] for x in lnodes]
        out += rnodes
        return out

    def mcs(self, cut_set):
        out = []
        remove_duplicates = []
        for i in cut_set:
            out.append(list(dict.fromkeys(i)))
        for cut_set in out:
            if cut_set not in remove_duplicates:
                remove_duplicates.append(cut_set)
        out = remove_duplicates
        return out

    def pretty_display(self, cut_sets):
        for i in range(len(cut_sets)):
            print('mcs_{}={}\n'.format(i, cut_sets[i]))


class Distributions(Gates):
    def __init__(self):
        pass

    def exp_dist(self, rate, t):
        return math.exp(rate * t)

    def prod_list(self, iterlist):
        result = 1
        for x in iterlist:
            result *= 1 - x
        return result

    def prob(self, mcs, distr_dict):
        prob_calc = 0
        for cut_set in mcs:
            prob_list = []
            for event in cut_set:
                prob_list.append(distr_dict[f"{event}"])
            prob_calc += self.prod_list(prob_list)
        return 1 - prob_calc


