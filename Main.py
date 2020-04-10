import time
import numpy as np
from functools import cmp_to_key

class Graph(object):

    def __init__(self,*args,**kwargs):
        self.node_neighbors = {}
        self.circle_list = ['0']

    def add_nodes(self,nodelist):

        for node in nodelist:
            self.add_node(node)

    def add_node(self,node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self,edge):
        u,v = edge
        if u in self.nodes():
            self.node_neighbors[u].append(v)
        else:
            self.node_neighbors[u] = [v]

    def nodes(self):
        return self.node_neighbors.keys()


    def check_circle(self):
        def DFS(x, in_circle, stack_index, path_stack):
            # visited[x] = True
            if stack_index == 6:
                return
            stack_index += 1
            path_stack[stack_index] = x       
            nodes_neighbors = self.node_neighbors[x]
            nodes_neighbors.sort()
            for node in nodes_neighbors:
                if node not in self.nodes():
                    continue
                if node == path_stack[0]:
                    if stack_index < 2:
                        continue
                    else:
                        # circle = path_stack[0: stack_index + 1]
                        # circle.append(node)
                        # self.circle_list.append(circle)
                        
                        self.circle_list.append(','.join(str(i) for i in path_stack[0: stack_index + 1]))
                        break
                else:
                    if node in in_circle:
                        continue
                    else:
                        DFS(node, in_circle, stack_index, path_stack)
            path_stack[stack_index] = 0
            stack_index -= 1

        path_stack = [0,0,0,0,0,0,0]
        in_circle = []
        stack_index = -1
        visited = {}
        for node in sorted(self.nodes()):
            in_circle.append(node)
            DFS(node, in_circle, stack_index, path_stack)
        g.circle_list[0] = str(len(g.circle_list) - 1)

    



    


if __name__ == '__main__':
    time_start = time.time()
    g = Graph()
    data = np.loadtxt('./data/test_data.txt', dtype=int, delimiter=',', usecols=[0,1])
    for edge in data:
        g.add_edge(edge)
    print(g.nodes())
    g.check_circle()
    # print(g.circle_list)
    np.savetxt('result.txt', sorted(g.circle_list, key=cmp_to_key(lambda a,b: a.count(',') - b.count(','))), delimiter=',', fmt='%s')
    print('total:', time.time() - time_start)