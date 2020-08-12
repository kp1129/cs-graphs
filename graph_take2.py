# this is a copy of graph.py from the projects directory

# utils for implementation: queue and stack
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


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# ________________________________________________________

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
            raise IndexError("nonexistent node :'(")    

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
        # remember that bft is not a search, it's
        # just a traversal. and because it's breadth-first
        # we use a queue

        # create a queue
        q = Queue()
        # enqueue starting_vertex
        q.enqueue(starting_vertex)
        # create a visited set
        visited = set()
        # while queue is not empty:
        while q.size() > 0:
            # dequeue the first vertex
            vertex = q.dequeue()
            # if it's not in visited set:
            if vertex not in visited:
                # visit it! and mark it as visited by adding it to visited set
                print(vertex)
                visited.add(vertex)
                # get all of its neighbors and enqueue them
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # remember that for depth first we use a stack
        # otherwise it's just like breadth-first traversal

        # create a stack 
        s = Stack()
        # add starting_vertex to the top of the stack 
        s.push(starting_vertex)
        # create visited set
        visited = set()

        # while stack is not empty:
        while s.size() > 0:
            # pop off the top vertex from the stack
            vertex = s.pop()
            # has it been visited before? if not:
            if vertex not in visited:
                # visit it! and add it to visited set
                print(vertex)
                visited.add(vertex)
                # get all of its neighbors, and for each one:
                for neighbor in self.get_neighbors(vertex):
                    # add them to the top of the stack
                    s.push(neighbor)

    # def dft_recursive(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.
    #     This should be done using recursion.
    #     """
    #     pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # this is similar to breadth-first traversal, but
        # it's not just traversing - it's trying different paths! how cool

        # the difference in terms of logic is that we keep track 
        # not only of the visited nodes but of the entire path
        # that we took to get here (track this in the queue)

        # create a queue
        q = Queue()
        # enqueue starting_vertex - but as a list
        q.enqueue([starting_vertex])
        # create a visited set
        visited = set()

        #while queue is not empty:
        while q.size() > 0:
            # dequeue the first path from the front of the queue
            path = q.dequeue()
            # grab the last vertex from that path,
            # which is the most recent neighbor added
            vertex = path[-1]            
            # if that vertex has not been visited:
            if vertex not in visited:
                # is this the destination vertex? if yes:
                if vertex == destination_vertex:
                    # return the entire path. we have found the shortest path
                    # to the destination
                    return path
                # else:
                else:
                    # visit it! and add it to visited set
                    print(vertex)
                    visited.add(vertex)
                    # get all of its neighbors and for each one:
                    for neighbor in self.get_neighbors(vertex):
                        # make a copy of the path
                        path_copy = path.copy()
                        # append the neighbor to the copy
                        path_copy.append(neighbor)
                        # enqueue the copy of the path with its neighbor added
                        q.enqueue(path_copy)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # remember, this is a search, not a traversal. we're looking for a PATH
        # also remember that for depth-first, we'll be using a stack rather than a queue

        # create a stack
        s = Stack()
        # push starting_vertex to the top of the stack
        # - but as a list
        s.push([starting_vertex])
        # create a visited set
        visited = set()

        #while stack is not empty:
        while s.size() > 0:
            # pop off the first path from the top of the stack
            path = s.pop()
            # grab the last vertex from that path,
            # which is the most recent neighbor added
            vertex = path[-1]            
            # if that vertex has not been visited:
            if vertex not in visited:
                # is this the destination vertex? 
                if vertex == destination_vertex:
                    # return the entire path. we have found the shortest path
                    # to the destination
                    return path
                # else:
                else:
                    # visit it! and add it to visited set
                    print(vertex)
                    visited.add(vertex)
                    # get all of its neighbors and for each one:
                    for neighbor in self.get_neighbors(vertex):
                        # make a copy of the path
                        path_copy = path.copy()
                        # append the neighbor to the copy
                        path_copy.append(neighbor)
                        # enqueue the copy of the path with its neighbor added
                        s.push(path_copy)

    # def dfs_recursive(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     This should be done using recursion.
    #     """
    #     pass  # TODO

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