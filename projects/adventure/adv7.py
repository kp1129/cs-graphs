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
my_path = []

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# keep repeating this until we find all 500 rooms
while len(visited_rooms) != len(room_graph):
      
    visited_rooms.add(player.current_room)      
    exits = player.current_room.get_exits()     
    current = player.current_room

    if 'n' in exits and current.get_room_in_direction('n') not in visited_rooms:
        my_path.append('n')
        traversal_path.append('n')
        player.current_room = current.get_room_in_direction('n')
    elif 'w' in exits and current.get_room_in_direction('w') not in visited_rooms:
        my_path.append('w')
        traversal_path.append('w')
        player.current_room = current.get_room_in_direction('w')
    elif 's' in exits and current.get_room_in_direction('s') not in visited_rooms:
        my_path.append('s')
        traversal_path.append('s')
        player.current_room = current.get_room_in_direction('s')
    elif 'e' in exits and current.get_room_in_direction('e') not in visited_rooms:
        my_path.append('e')
        traversal_path.append('e')
        player.current_room = current.get_room_in_direction('e')
    else:
          # no more unexplored rooms left
          # traverse back 
        reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        d = my_path.pop()
        reversed_d = reverse_direction[d]
        traversal_path.append(reversed_d)
        player.current_room = player.current_room.get_room_in_direction(reversed_d)


for move in traversal_path:
    player.travel(move)
    print('moving ', move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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