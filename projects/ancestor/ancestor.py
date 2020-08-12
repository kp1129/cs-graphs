# utils for implementation: queue, stack, and graph
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
    def __init__(self):
        # dictionary of vertices
        # the key is the vertex in question
        # and the value is a set of all of its neighbors
        # (adjacency list)
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # vertices will be numeric, so vertex_id
        # initialize a vertex's neighbors as empty set
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # add a connection between vertices
        # remember we're using the adjacency list pattern
        # adding an edge means that the vertex we're connecting TO
        # should be added to the set of neighbors to the vertex
        # we are connecting FROM.

        # first, check to make sure these vertices exist
        # if not, raise index error
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")    

    def get_ancestors(self, vertex_id):
        return self.vertices[vertex_id]        

    # a way to traverse the graph
    # breadth-first traversal
    def bft(self, starting_vertex_id):
        # create an empty queue
        q = Queue()
        # add starting_vertex_id to the queue
        q.enqueue(starting_vertex_id)
        # create set for visited vertices
        visited = set()
        # while queue is not empty:
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if it's not in visited:
            if v not in visited:
                # visited it! whatever visiting means
                # for our purposes, we can just print it.
                print(v)
                # so that's the first part. part 2 of visiting
                # a node is adding it to visited set
                visited.add(v)
                # add all of it's unvisited neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    if neighbor not in visited:
                        q.enqueue(neighbor)

    # another way to traverse the graph!
    # depth-first traversal
    def dft(self, starting_vertex_id):
        # the logic is actually all the same,
        # except instead of a queue we're using a stack
        
        # create a stack
        s = Stack()
        # put the starting vertex at the top of the stack
        s.push(starting_vertex_id)
        # create a visited set
        visited = set()
        # while stack is not empty:
        while s.size() > 0:
            # pop off the top item in the stack
            v = s.pop()
            # if it is not in visited:
            if v not in visited:
                # visit it! don't forget to add it to visited
                print(v)
                visited.add(v)
                # go through its neighbors:
                for neighbor in self.get_neighbors(v):
                    # if they're not already in visited,
                    # add them to the top of the stack
                    if neighbor not in visited:
                        s.push(neighbor)



def earliest_ancestor(ancestors, starting_node):
    # first, take ancestors, which is a list of tuples
    # and for each tuple, add 2 vertices and an edge from
    # the first vertex (parent) to the 2nd vertex (child)

    # if i do this right, i should end up with an adjacency list
    # representation that connects nodes in the same way as the
    # visualization in the readme.

    # after creating this and printing it out, i think i need to reverse the graph
    # so that the connection isn't from parent to child but from child to parent
    # otherwise, since this is a directed graph i cannot get back up to the parent
    # from it's "child" node
    
    g = Graph()

    for pair in ancestors:
        g.add_vertex(pair[0]) # parent
        g.add_vertex(pair[1]) # child
        # one-way connection from child to parent
        g.add_edge(pair[1], pair[0]) 
    # so far so good
    # now the node edges are one way connection to their parents

    q = Queue()
    q.enqueue([starting_node])
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            parents = g.get_ancestors(v)

            if len(parents) == 0:
                # if node has no parents and it's our initial node
                if v == starting_node:
                    return -1
                else:
                    return v

            else:
                visited.add(v)

                for parent in parents:
                    new_path = path.copy()
                    new_path.append(parent)
                    q.enqueue(new_path)    


    # where i left off:
    # in the case of two parents, it's returning the 'shortest path' instead of 
    # exploring the parents of the other parent
    # this is the test that's failing: self.assertEqual(earliest_ancestor(test_ancestors, 3), 10) 
    # mine returns 2 instead of 10






    # #
    # # starting with the starting_node, get it's edges/neighbors that it's connected to. check to see if they have edges/ancestors
    # result = g.get_ancestors(starting_node)
    # # if there are no known ancestors
    # if len(result) == 0:
    #     return -1
    # # if only one known ancestor 
    # elif len(result) == 1:
    #     return result[0]
    # else:    
    #     has_ancestors = True
    #     parents = result
    #     while has_ancestors:
    #         for parent in parents:
    #             new_result = g.get_ancestors(parent)
                


    # # if there are known ancestors
    # if len(result) > 0:
    #     # for each ancestor, check their ancestors
    #     for i in range(len(result)): #because we don't know if there's one known ancestor or two
    #         g.get_ancestors(result[i])
    #     pass
    # # there are no known ancestors
    # # as per the problem requirements, return -1
    # else:
    #     return -1

        

    # for each of the neighbors, get their edges/neighbors

    # keep going through the levels of neighbors until you get to the one parent whose ancestors/neighbors are an empty set
    
    

sample_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]    

print(earliest_ancestor(sample_pairs, 1))   

