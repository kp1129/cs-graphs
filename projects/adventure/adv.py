from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import os

dirpath = os.path.dirname(os.path.abspath(__file__))

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file =  dirpath + "/maps/test_line.txt"
# map_file = dirpath + "/maps/test_cross.txt"
map_file = dirpath + "/maps/test_loop.txt"
# map_file = dirpath + "/maps/test_loop_fork.txt"

# the final boss map, uncomment when ready
# map_file = dirpath + "/maps/main_maze.txt"

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

class Queue:
    def __init__(self):
        self.queue= []
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
        # adds a vertex/room to the graph
        self.vertices[vertex_id] = {}
        # build a vertex's neighbors/exit dictionary
        exits_list = player.current_room.get_exits()
        for exit in exits_list:
            self.vertices[vertex_id][exit] = "?"         

    def add_edge(self, v1, d, v2):
        directions_dict = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][d] = v2
            reverse_d = directions_dict[d]
            self.vertices[v2][reverse_d] = v1
        else:
            raise IndexError("nonexistent vertex")     

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bfs(self, cardinal_direction, visited_rooms):
        q = Queue()
        q.enqueue([cardinal_direction])
        while q.size() > 0:
            path = q.dequeue()
            d = path[-1]
            player.travel(d)
            cr = player.current_room.id

            if cr not in visited_rooms:
                print('the path to get here, ' path)
                return path
            else:
                neighbors = self.get_neighbors



    def bfs(self, starting_vertex_id, visited_rooms):
        unexplored = "?"
        q = Queue()
        q.enqueue([starting_vertex_id])
        print('starting vertex id ', starting_vertex_id)
        

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v == "?":
                return path
            else:    

                visited_rooms.add(v)
                neighbors = self.get_neighbors(v)
                neighbors_list = list(neighbors.values())
                for neighbor in neighbors_list:
                    # if neighbor == "?":
                    #     return path[:-1]
                    print('adding neighbor to queue ', neighbor, self.vertices[v])                    
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)


            # if v not in visited_rooms:
            #     if v == "?":
            #         print('what is going on?? ', v)
            #         # if v == unexplored:
            #         return path
            # else:    
            #     print('im at ', v)
                
            #     visited_rooms.add(v)
            #     neighbors = self.get_neighbors(v)
            #     neighbors_list = list(neighbors.values())
            #     for neighbor in neighbors_list:
            #         if neighbor not in visited_rooms:
            #             print('adding new neighbor ', neighbor)
            #             path_copy = list(path)
            #             path_copy.append(neighbor)
            #             q.enqueue(path_copy)

    def dft(self, cardinal_direction, visited_rooms):        
        s = Stack()        
        s.push(cardinal_direction)
        traversal_path.append(cardinal_direction) 
        
        while s.size() > 0:           
            d = s.pop()
            pr_id = player.current_room.id         
            player.travel(d)
            cr_id = player.current_room.id            
            if cr_id not in visited_rooms:
                print(cr_id)
                self.add_vertex(cr_id)
                self.add_edge(pr_id, d, cr_id)
                visited_rooms.add(cr_id)               
                neighbors = self.get_neighbors(cr_id)
                for direction, room in neighbors.items():
                    if room == "?":
                        s.push(direction)
                        traversal_path.append(direction) 
        print('dead end!')             
        # print('currently stuck in room ', player.current_room.id, " and awaiting further instructions")
       
# create a graph
g = Graph()
visited_rooms = set()
player.current_room = world.starting_room
vertex_id = player.current_room.id
exits = player.current_room.get_exits()
visited_rooms.add(vertex_id)
g.add_vertex(vertex_id)
for exit in exits:
    g.vertices[vertex_id][exit] = "?"
g.dft(exits[0], visited_rooms)

def translate_bfs_to_directions(list_of_rooms):
    for i in range(len(list_of_rooms) - 2):
        exits = g.get_neighbors(list_of_rooms[i])
        for direction, room in exits.items():
            if room == list_of_rooms[i + 1]:
                traversal_path.append(direction)
                player.travel(direction)

def choose_new_direction(current_room_id):
    exits = g.vertices[current_room_id]
    for direction, room in exits.items():
        if room == '?':
            return direction
counter = 0
while len(visited_rooms) != len(room_graph) and counter < 15:
    stuck_in = player.current_room.id
    # exits = player.current_room.get_exits()
    hanging_out = g.bfs(stuck_in, visited_rooms)
    translate_bfs_to_directions(hanging_out)
    need_direction = choose_new_direction(player.current_room.id)
    g.dft(need_direction, visited_rooms)
    counter +=1

print(visited_rooms)
print(len(visited_rooms))
print(len(room_graph))

#_____________________________________________________________
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
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
