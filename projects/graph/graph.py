"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex Id
        # Create an empty set to store visited vertices
        # While the queue is not empty...
            #Dequeue the first vertex
            #If that vertex has not been visited...
                # Mark it as visited
                # Then add all of its neighbors to the back of the queue.
        #queue first in first out.....

        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                # print(v)
                visited.add(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex
        # Create a Set to store visited vertices
        # While the stack is not empty...
        #     Pop the first vertex
        #     If that vertex has not been visited..
        #         Mark it as visited..
        #         Then add all of its neighbors to the top of the stack.
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        # print('dft')
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                # print(v)
                visited.add(v)
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        def innerRecursive(vertex):
            if vertex in visited:
                return 
            else:
                visited.add(vertex)
                # print(vertex)
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        innerRecursive(neighbor)

        innerRecursive(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create an empty queue and enqueue A PATH TO the starting vertex ID
        #Create a set to store the visited vertices
        #While the queue is not empty...
            #Dequeue the first path
            #Grab the last vertex from the PATH
            #If the vertex has not been visited..
                # Check if its the Target
                #     if so return path
                #   Mark as visiited...and
                #   Then add a path to its neighbors to the back of the queue
                #   copy the path
                #   append the neighbor to the back....
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        if starting_vertex == destination_vertex:
            return starting_vertex
        
        while q.size() > 0:
            v = q.dequeue()
            if v[-1] not in visited:
                visited.add(v[-1])
                for neighbor in self.vertices[v[-1]]:
                    vList = v.copy()
                    vList.append(neighbor)
                    if neighbor == destination_vertex:
                        return vList
                    else:
                        q.enqueue(vList)

          
              

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v[-1] not in visited:
                visited.add(v[-1])
                for neighbor in self.vertices[v[-1]]:
                    vList = v.copy()
                    if neighbor == destination_vertex: 
                        vList.append(neighbor)
                        return vList
                    else:
                        vList.append(neighbor)
                        s.push(vList)


    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
