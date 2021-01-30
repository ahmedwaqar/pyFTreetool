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

    def exp_dist(self,rate,t):
           return math.exp(rate*t)






if __name__ == "__main__":
    z = Gates()
    a = [['a', 'b', 'c'], ['c', 'd']]
    b = [['e', 'f', 'g'], ['h', 'i']]
    out = z.and_gate(a, b)
    print(out)
    out = z.or_gate(out, b)
    out = z.or_gate(out, b)
    z.pretty_display(out)
    out = z.mcs(out)
    z.pretty_display(out)
    distr = Distributions()
    calc_distr = distr.exp_dist(-2.5,5)
    print(calc_distr)

