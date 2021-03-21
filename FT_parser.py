import re
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import sys
import netgraph

f_path = '/Users/waqarahmed/Documents/tools/python/FT_tool/FTree.py'

class GenerateFT:
    def __init__(self):
        pass

    def split_on_condition(self, seq, condition):
        a, b = [], []
        for item in seq:
            (a if condition(item) else b).append(item)
        return a, b

    def partition_cond(self, ft_list, cond):
        new_list = []
        part_list = []
        for  x in ft_list:
            if x in [cond]:
                new_list.append(part_list)
                part_list = []
                continue
            part_list.append(x)
        return new_list

    def add_nodes(self, G, list):
        G.add_nodes_from(list)

    def add_edges(self, G, list):
        edge_list = []
        edge_list = edge_list + ([(list[0], list[1])])
        for x in list[2:]:
            edge_list = edge_list + ([(list[1], x)])
        G.add_edges_from(edge_list)

    def print_FT(self, file_path):
        ft_frag = []

        with open(file_path) as file:
            regex = r'([a-zA-Z]+\.((and)|(or))_gate)'
            gates_search = [lines for lines in file if re.search(regex, lines)]
            # clean the data extracted from program file
            clean_ft = [i for i in gates_search if not re.search('^([#])', i)]
            for i in clean_ft:
                ft_frag += re.split('=|,|\(|\)', i)
            ft_frag = [r.strip() for r in ft_frag ]
            print(ft_frag)
            ft_frag_t = []
            for r in ft_frag:
                if '[' in r:
                   ft_frag_t.append(r.split('[')[-1])
                elif ']' in r:
                    ft_frag_t.append(r.split(']')[0])
                else:
                    ft_frag_t.append(r)
            ft_frag = ft_frag_t
            print(ft_frag_t)

            temp = []
            index = 1
            for i in ft_frag:
                if i == "z.and_gate" or i == "z.or_gate":
                   temp.append(i.split('.')[-1]+str(index))
                   index += 1
                else:
                    temp.append(i)
            ft_frag = temp
            print(ft_frag)
            ft_split_pairs = self.split_on_condition(ft_frag, lambda x: x not in [''])
            part_ft = self.partition_cond(ft_frag, '')
            G = nx.DiGraph()
            for i in part_ft:
                self.add_nodes(G, i)
                self.add_edges(G, i)
            plt.subplot(111)
            write_dot(G, 'test.dot')

            # same layout using matplotlib with no labels
            plt.title('Fault Tree Diagram')
            pos = graphviz_layout(G, prog='dot')
            options = {
                'node_size': 100,
                'width': 3,
            }
            nx.draw(
                G,
                pos,
                with_labels=True,
                arrows=True,
                # cmap=plt.cm.Blues,
                # node_color=range(len(G)),
                # **options,
                node_shape="s",
                node_color='none',
                bbox=dict(
                    facecolor='none', edgecolor='black', boxstyle='round,pad=1'
                ),
            )
            plt.show()
            # plt.savefig('nx_test.png')


if __name__ == "__main__":
    gen_ft = GenerateFT()
    gen_ft.print_FT(f_path)
