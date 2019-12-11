# //bfs //bft
# Clarifications:
# * The input will not be empty.
# * There are no cycles in the input.
# * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# * IDs will always be positive integers.
# * A parent may have any number of children.

# NONCYCLIC, directed towards the parents......
#Fifo
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('NO vertices')

    def bfs(self, starting_node):
        
        q = Queue()
        q.enqueue(starting_node)
        visited = set()
        topAncestorList = [starting_node]
        
        while q.size() > 0:
            v = q.dequeue()
            # print(v)
            tempList = []
            if v not in visited:
                visited.add(v)
                for item in self.vertices[v]: #go back and put in temp list then sort them to lowest to high then loop through and find the lowest to place at the back of the list.
                    # topAncestorList.append(item)
                    # q.enqueue(item)
                    tempList.append(item)
                tempList.sort()
                i = len(tempList) - 1
                while i > -1:
                    topAncestorList.append(tempList[i])
                    q.enqueue(tempList[i])
                    i -= 1
                if len(topAncestorList) == 1:
                    return -1
        # print(topAncestorList)
        return topAncestorList[-1]



def earliest_ancestor(ancestors, starting_node):
    
    graph = Graph()
    for i in range(12):
        graph.add_vertex(i)
    for i in ancestors:
        graph.add_edge(i[1], i[0])

    earliest_ancestor = graph.bfs(starting_node)
    return earliest_ancestor



earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 5)

