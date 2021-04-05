from abc import ABC
import math
import itertools


class AbstractGates(ABC):
    def and_gate(self):
        pass

    def or_gate(self):
        pass


class Gates(AbstractGates):
    def __init__(self):
        pass

    def pairwise(self, iterable):
        "s -> (s0, s1), (s2, s3), (s4, s5), ..."
        a = iter(iterable)
        return itertools.zip_longest(a, a)

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

    def and_gate_opt(self, lnodes, rnodes):
        out = []
        for i in lnodes:
            for r in rnodes:
                out.append(i + r)
        return out

    def or_gate(self, lnodes, rnodes):
        out = [x[:] for x in lnodes]
        out += rnodes
        return out

    def sort_sublists(self, input_list):
        result = list(map(sorted, input_list))
        return result

    def mcs(self, cut_set):
        out = []
        remove_duplicates = []
        cut_sets = self.sort_sublists(cut_set)
        for i in cut_sets:
            out.append(list(dict.fromkeys(i)))
        for cut_set in out:
            if cut_set not in remove_duplicates:
                remove_duplicates.append(cut_set)
        temp = [x[:] for x in remove_duplicates]
        for a, b in itertools.combinations(temp, 2):
            try:
                if set(a) <= set(b):
                    temp.remove(b)
                elif set(b) <= set(a):
                    temp.remove(a)
            except:
                continue
        return temp

    def mcs_opt(self, cut_set):
        import itertools

        cut_set.sort()
        print(cut_set)
        return list(k for k, _ in itertools.groupby(cut_set))

    def pretty_display(self, cut_sets):
        for i in range(len(cut_sets)):
            print("mcs_{}={}\n".format(i, cut_sets[i]))


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
