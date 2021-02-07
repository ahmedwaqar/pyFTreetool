import re
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import sys

f_path = '/Users/waqarahmed/Documents/tools/python/FT_tool/FTree.py' 

class GenerateFT:
    def __init__(self):
        pass

    def split_on_condition(self, seq, condition):
        a, b = [], []
        for item in seq:
            (a if condition(item) else b).append(item)
        return a, b

    def partition_cond(self, list, cond):
        part_list = []
        for x in list:
            if x in [cond]:
                part_list.append(list[: list.index(x)])
        return part_list

    def add_nodes(self, G, list):
        G.add_nodes_from(list)

    def add_edges(self, G, list):
        edge_list = []
        edge_list = edge_list + ([(list[0], list[1])])
        for x in list[2:]:
            edge_list = edge_list + ([(list[1], x)])
        print(edge_list)
        G.add_edges_from(edge_list)

    def print_FT(self, file_path):
        ft_frag = []

        with open(file_path) as file:
            regex = r'([a-zA-Z]+\.((and)|(or))_gate)'
            gates_search = [lines for lines in file if re.search(regex, lines)]
            print(gates_search)
            # clean the data extracted from program file
            clean_ft = [i for i in gates_search if not re.search('^([#])', i)]
            print(clean_ft)
            for i in clean_ft:
                ft_frag = ft_frag + re.split('=|,|\(|\)', i)

            print(ft_frag)
            ft_split_pairs = self.split_on_condition(ft_frag, lambda x: x not in ['\n'])
            print(ft_split_pairs)
            part_ft = self.partition_cond(ft_frag, '\n')
            print(part_ft)
            G = nx.DiGraph()
            self.add_nodes(G, part_ft[0])
            plt.subplot(121)
            write_dot(G, 'test.dot')

            # same layout using matplotlib with no labels
            plt.title('draw_networkx')
            pos = graphviz_layout(G, prog='dot')
            nx.draw(
                G,
                pos,
                with_labels=True,
                arrows=True,
                node_size=2000,
                cmap=plt.cm.Blues,
                node_color=range(len(G)),
            )
            plt.savefig('nx_test.png')


if __name__ == "__main__":
    gen_ft = GenerateFT()
    gen_ft.print_FT(f_path)
    

    
