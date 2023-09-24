'''
파일명: Ex21-8-Graph.py

그래프(Graph)
    노드(vertice)와 간선(edge)로
    이루어진 자료구조
'''
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        '''
         self.adj_list[vertex] = {'A':[B,],'B':[A,],'C':[],'D':[],'E':[]}
        '''
        for vertex in vertices:
            self.adj_list[vertex] = []

    '''
    add_edge('A', 'B')
        self.adj_list['A'].append('B')
        self.adj_list['B'].append('A')
    '''
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, end=' -> ')
            print(' -> '.join(str(node) for node in self.adj_list[vertex]))

# 실행코드
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')

'''
{
    A:[B, C],
    B:[A, D],
    C:[A, D, E],
    D:[B, C],
    E:[C]
}
'''

graph.print_graph()