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
# map_file = dirpath + "/maps/test_loop.txt"
# map_file = dirpath + "/maps/test_loop_fork.txt"

# the final boss map, uncomment when ready
map_file = dirpath + "/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = set()

def dft(starting_room):
    stack = []
    # add starting_vertex to the top of the stack 
    stack.append(starting_vertex)
    

    # while stack is not empty:
    while len(stack) > 0:
        # pop off the top vertex from the stack
        vertex = stack.pop()
        # has it been visited before? if not:
        if vertex not in visited:
            # visit it! and add it to visited set
            print(vertex)
            visited.add(vertex)
            # get all of its neighbors, and for each one:
            for neighbor in self.get_neighbors(vertex):
                # add them to the top of the stack
                stack.append(neighbor)



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



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")