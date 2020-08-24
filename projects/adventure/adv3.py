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
# ____________________

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


def dftpath(current):
    visited_rooms.add(current)
    s = []
    l = current.get_exits()
    for i in l:
        s.append(current.get_room_in_direction(i))
    for neighbor in s:
        # if it's not visited
        traversal_path.append(l[s.index(neighbor)])
        if neighbor not in visited_rooms:
            # recurse on the neighbor
            dftpath(neighbor)


for move in traversal_path:
    player.travel(move)
visited_rooms.add(player.current_room)


dftpath(player.current_room)
if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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