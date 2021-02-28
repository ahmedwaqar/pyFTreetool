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

    def and_gate_json(self, ljson, rjson):
        out_json = self.and_gate(ljson['events'], rjson['events'])

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


if __name__ == "__main__":
    z = Gates()
    a = [['a', 'b', 'c'], ['c', 'd']]
    b = [['e', 'f', 'g'], ['h', 'i']]
    out = z.and_gate(a, b)
    out = z.or_gate(out, b)
    out = z.or_gate(out, b)
    z.pretty_display(out)
    out = z.mcs(out)
    z.pretty_display(out)
    distr = Distributions()
    calc_distr = distr.exp_dist(0, 5)
    product = distr.prod_list([1.0, 0.4, 0.6])
    print(f"value of product = {product}")
    distr_dict = {
        'a': 1 - distr.exp_dist(-0.5, 5),
        'b': 1 - distr.exp_dist(-0.2, 5),
        'c': 1.0,
        'd': 1 - distr.exp_dist(-0.4, 5),
        'e': 1 - distr.exp_dist(-0.3, 5),
        'f': 1 - distr.exp_dist(-0.2, 5),
        'g': 1 - distr.exp_dist(-0.3, 5),
        'h': 1 - distr.exp_dist(-0.33, 5),
        'i': 1 - distr.exp_dist(-0.2, 5),
    }
    prob_value = distr.prob(out, distr_dict)
    print(prob_value)
