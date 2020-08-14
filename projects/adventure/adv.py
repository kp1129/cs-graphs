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
map_file = dirpath + "/maps/test_cross.txt"
# map_file = dirpath + "/maps/test_loop.txt"
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
        self.vertices[vertex_id] = {}
        # build a vertex's neighbors/exit dictionary
        exits_list = player.current_room.get_exits()
        for exit in exits_list:
            self.vertices[vertex_id][exit] = "?"
         

    def add_edge(self, v1, d, v2):
        # adds an edge/exit to another vertex/room
        # remember that if we can go from room v1 to room v2
        # that means we can also go from room v2 to room v1
        # i.e., the edges and the graph as a whole is undirected
        # and when adding v2 as a neighbor to v1 we need to also
        # add v1 as a neighbor to v2
        directions_dict = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][d] = v2
            reverse_d = directions_dict[d]
            self.vertices[v2][reverse_d] = v1
        else:
            raise IndexError("nonexistent vertex")     

    def get_neighbors(self, vertex_id):
        # returns the neighbors/exit dictionary for given vertex_id 
        return self.vertices[vertex_id]



    def dft(self, cardinal_direction):
        # depth-first traversal

        # create a stack
        s = Stack()
        # put the starting vertex id on top of the stack
        s.push(cardinal_direction)
        # create a visited set
        visited = set()

        starting_room = player.current_room.id
        self.add_vertex(starting_room)
        traversal_path.append(cardinal_direction) 
        # while stack is not empty:
        while s.size() > 0:
            # pop the top item off the stack
            d = s.pop()
            pr_id = player.current_room.id
            print('going ', d)
            
            player.travel(d)
            cr_id = player.current_room.id
            # if it is not in visited:
            if cr_id not in visited:
                # visit it! add it to visited
                print(cr_id)
                self.add_vertex(cr_id)
                self.add_edge(pr_id, d, cr_id)
                visited.add(cr_id)
                # go through its neighbors. for each:
                neighbors = self.get_neighbors(cr_id)
                for direction, room in neighbors.items():
                    # if they're not already visited, 
                    # add them to the top of the stack
                    if room == "?":
                        s.push(direction)
                        traversal_path.append(direction) 
        print('dead end!')
        print(self.vertices)   
        print('traversal path: ', traversal_path)

    # def dft(self, starting_vertex_id):
    #     # depth-first traversal

    #     # create a stack
    #     s = Stack()
    #     # put the starting vertex id on top of the stack
    #     s.push(starting_vertex_id)
    #     # create a visited set
    #     visited = set()

    #     # while stack is not empty:
    #     while s.size() > 0:
    #         # pop the top item off the stack
    #         room = s.pop()
    #         # if it is not in visited:
    #         if room not in visited:
    #             # visit it! add it to visited
    #             print(room)
    #             self.add_vertex(room)
    #             visited.add(room)
    #             # go through its neighbors. for each:
    #             neighbors = self.get_neighbors(room)
    #             for direction, room in neighbors.items():
    #                 # if they're not already visited, 
    #                 # add them to the top of the stack
    #                 s.push(room)
    #                 traversal_path.append(direction)


# create a graph
g = Graph()
player.current_room = world.starting_room
vertex_id = player.current_room.id
exits = player.current_room.get_exits()
g.dft(exits[0])









# visited_rooms = set()    

# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)
# # starting vertex id
# vertex_id = player.current_room.id
# g.add_vertex(vertex_id)
# exits = player.current_room.get_exits()
# # for each exit available, add the direction : ? pairs 
# # as neighbors for this vertex id
# exits_dict = {}
# for each in exits:
#     exits_dict[each] = "?"
# g.vertices[vertex_id] = exits_dict

# travel_direction = 's'
# player.travel(travel_direction)
# prev_room_id = vertex_id
# traversal_path.append(travel_direction)
# vertex_id = player.current_room.id
# visited_rooms.add(player.current_room)
# g.add_vertex(vertex_id)
# exits = player.current_room.get_exits()
# # for each exit available, add the direction : ? pairs 
# # as neighbors for this vertex id
# exits_dict = {}
# for each in exits:
#     exits_dict[each] = "?"
# g.vertices[vertex_id] = exits_dict
# g.vertices[prev_room_id][travel_direction] = vertex_id
# g.vertices[vertex_id]['n'] = prev_room_id
# print('progress? ', g.vertices)
# print('directions: ', traversal_path)
# print('visited rooms ', visited_rooms)

# def explore_dft(curr_room_obj):
    
#     # what are all the exits in this room?
#     s = Stack()
#     s.push(curr_room_obj)

#     while s.size() > 0:
#         curr_room = s.pop()
#         # enter the room, get room id
#         player.travel()
#         if curr_room not in visited_rooms:
#             visited_rooms.add(curr_room)
#             # equivalent of get_neighbors
#             available_exits = player.current_room.get_exits()
#             try_this_direction = ''
#             for each_exit in available_exits:
#                 if each_exit not in visited_rooms[curr_room]:
#                     visited_rooms[curr_room][each_exit] = "?"
#                     try_this_direction = each_exit
#                     player.travel(try_this_direction)
#                     new_room_id = player.current_room.id
#                     s.push(new_room_id)




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
