from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"

# the final boss map, uncomment when ready
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

#_____________________________________________________________
# Fill this out with directions to walk

# traversal_path = ['n', 'n']
traversal_path = []

class Stack:
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

class Graph:
    def __init__(self):
        # an adjacency list
        # a dictionary where keys = room id's
        # and values are a set/dictionary of 
        # exit direction : room id it leads to

        # if there's no exit in a direction, that 
        # direction is not listed in the dictionary
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # adds a vertex/room to the graph
        # initialize a vertex's neighbors/exit dictionary
        # as an empty set
        self.vertices[vertex_id] = set() 

    def add_edge(self, v1, v2):
        # adds an edge/exit to another vertex/room
        # remember that if we can go from room v1 to room v2
        # that means we can also go from room v2 to room v1
        # i.e., the edges and the graph as a whole is undirected
        # and when adding v2 as a neighbor to v1 we need to also
        # add v1 as a neighbor to v2
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("nonexistent vertex")     

    def get_neighbors(self, vertex_id):
        # returns the neighbors/exit dictionary for given vertex_id 
        return self.vertices[vertex_id]

    def dft(self, starting_vertex_id):
        # depth-first traversal

        # create a stack
        s = Stack()
        # put the starting vertex id on top of the stack
        s.push(starting_vertex_id)
        # create a visited set
        visited = set()

        # while stack is not empty:
        while s.size() > 0:
            # pop the top item off the stack
            room = s.pop()
            # if it is not in visited:
            if room not in visited:
                # visit it! add it to visited
                visited.add(room)
                # go through its neighbors. for each:
                neighbors = self.get_neighbors(room)
                for neighbor in neighbors:
                    # if they're not already visited, 
                    # add them to the top of the stack
                    s.push(neighbor)


# create a graph
g = Graph()
visited_rooms = set()    

player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# starting vertex id
vertex_id = player.current_room.id
print('current room id: ', player.current_room.id)
print('current room: ', player.current_room)
print('exits available: ', player.current_room.get_exits())
g.add_vertex(vertex_id)


exits = player.current_room.get_exits()
# for each exit available, add the direction : ? pairs 
# as neighbors for this vertex id
exits_dict = {}
for each in exits:
    exits_dict[each] = "?"
g.vertices[vertex_id] = exits_dict
print('progress? ', g.vertices)




#_____________________________________________________________
# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
#_____________________________________________________________    

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
