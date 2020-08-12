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
    def __init__(self):
        # dictionary of vertices
        # the key is the vertex in question
        # and the value is a set of all of its neighbors
        # (adjacency list)
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # vertices will be numeric, so vertex_id
        # initialize a vertex's neighbors as empty set
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

    def get_neighbors(self, vertex_id):
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



# time to instantiate a new graph!
g = Graph()
# populate it with vertices
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
# add edges
g.add_edge(1, 2)
# if this is undirected graph (meaning edges go both ways)
# add g.add_edge(2, 1) to add 1 as 2's neighbor/edge
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(3, 6)
g.add_edge(6, 5)
g.add_edge(5, 4)


print(g.vertices)

# g.bft(1)
# g.bft(3)

