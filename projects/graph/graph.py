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
        # breadth-first uses a queue
        q = Queue()
        # start with starting_vertex
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            # dequeue the first item
            item = q.dequeue()
            if item not in visited:
                visited.add(item)
                print(item)

                for next_vortex in self.get_neighbors(item):
                    q.enqueue(next_vortex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # depth-first uses a stack
        s = Stack()
        # begin with starting_vertex
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            # grab the first item from the stack
            item = s.pop()
            if item not in visited:
                visited.add(item)
                print(item)

                for next_vortex in self.get_neighbors(item):
                    s.push(next_vortex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if starting_vertex not in visited:
        #     visited.add(starting_vertex)
        #     print(starting_vertex)

        #     neighbors = self.get_neighbors(starting_vertex)
        #     for each in neighbors:
        #         self.dft_recursive(each, visited)

        visited.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        # enqueue the starting vertex, but
        # not by itself -- as a list. the list
        # is to keep track of the verteces we visit
        # to get to the destination vertex (because we
        # need a collection where the order matters)
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            # lst represents the [] with vertices in 
            # the path to destination vertex
            lst = q.dequeue()
            # remove the last vertex because that's the
            # one added most recently
            v = lst[-1]

            if v not in visited:
                if v == destination_vertex:
                    # if we found the destination, 
                    # return the whole path that it took to get here
                    return lst
                else:
                    visited.add(v)
                    
                # queue up the next vertices
                for next_vertex in self.get_neighbors(v):
                    new_lst = lst.copy()
                    # update list that keeps track of path with latest vertex
                    new_lst.append(next_vertex)
                    # add the updated list path to the queue
                    q.enqueue(new_lst)

        return None            

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        # add the starting vertex to stack, but
        # not by itself -- as a list. the list
        # is to keep track of the verteces we visit
        # to get to the destination vertex (because we
        # need a collection where the order matters)
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            # lst represents the [] with vertices in 
            # the path to destination vertex
            lst = s.pop()
            # remove the last vertex because that's the
            # one added most recently
            v = lst[-1]

            if v not in visited:
                if v == destination_vertex:
                    # if we found the destination, 
                    # return the whole path that it took to get here
                    return lst
                else:
                    visited.add(v)
                    
                # queue up the next vertices
                for next_vertex in self.get_neighbors(v):
                    new_lst = lst.copy()
                    # update list that keeps track of path with latest vertex
                    new_lst.append(next_vertex)
                    # add the updated list path to the queue
                    s.push(new_lst)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        visited.add(starting_vertex)
        # path.append(starting_vertex)
        # not sure why the line above doesn't work??
        # but this was the only fix i could find
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        else:
            for each in self.get_neighbors(starting_vertex):
                if each not in visited:
                    result = self.dfs_recursive(each, destination_vertex, visited, path)    
                    if result is not None:
                        return result

      



        # if len(path) == 0:
        #     path.append(starting_vertex)
        #     s.push(path)

        # while s.size() > 0:
        #     lst = s.pop()
        #     v = lst[-1]

        #     if v not in visited:
        #         if v == destination_vertex:
        #             return lst
        #     else:
        #         visited.add(v)

        #         for next_vertex in self.get_neighbors(v):
        #             new_lst = lst.copy()
        #             new_lst.append(next_vertex)
        #             s.push(new_lst) 
        #             result = self.dfs_recursive(next_vertex, destination_vertex, visited, s, new_lst)  
        #             if result is not None: 
        #                 return result     

        # return
        # ________________________________
        # if len(path) == 0:
        #     path.append(starting_vertex)
        
        # v = path[-1]

        # if v not in visited:
        #     if v == destination_vertex:
        #         return path
        #     else:
        #         visited.add(v)

        #     neighbors = self.get_neighbors(v)
        #     for each in neighbors:
        #         if each not in visited:
        #             path.append(each)
        #             result = self.dfs_recursive(each, destination_vertex, visited, path)
        #             if result is not None:
        #                 return result
        
        #     return        



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
    print("\n")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("\n")
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
    print("dfs recursive", graph.dfs_recursive(1, 6))
