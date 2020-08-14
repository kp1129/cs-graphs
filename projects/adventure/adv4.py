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

explored_rooms = {}
reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
my_path = []

# helper functions
def add_vertex(room_id):
    explored_rooms[room_id] = {}
def add_edge(room1, direction, room2):
    if room1 in explored_rooms and room2 in explored_rooms:
        explored_rooms[room1][direction] = room2
        reverse = reverse_direction[direction]
        explored_rooms[room2][reverse] = room1

    
def dft(explored_rooms, my_path):
    traversing = True

    while traversing:

        if player.current_room.id not in explored_rooms:       
            add_vertex(player.current_room.id)
        # print('currently in ', player.current_room.id)
        unexplored_direction = None    
        for exit in player.current_room.get_exits():
            if exit not in explored_rooms[player.current_room.id]:                
                explored_rooms[player.current_room.id][exit] = '?'
                
            if explored_rooms[player.current_room.id][exit] == '?':
                unexplored_direction = exit    
        if unexplored_direction is not None:
            prev_room = player.current_room.id
            my_path.append(unexplored_direction)
            player.travel(unexplored_direction)
            new_room = player.current_room.id
            if new_room not in explored_rooms:
                add_vertex(new_room)
                add_edge(prev_room, unexplored_direction, new_room)
            if explored_rooms[prev_room][unexplored_direction] == '?':    
                add_edge(prev_room, unexplored_direction, new_room)    

        else:    
            traversing = False
            return True
dft(explored_rooms, my_path)          

all_explored = True
queue = []
def backup_bfs(explored_rooms, my_path, all_explored, queue):
    
    my_path_copy = list(my_path)
    while all_explored:
        rev = my_path_copy.pop()
        rev = reverse_direction[rev]
        my_path.append(rev)
        player.travel(rev)
        currently_in = player.current_room.id
        for exit_direction, exit_room in explored_rooms[currently_in].items():
            if exit_room == '?':
                player.travel(direction)
                new_room = player.current_room.id
                add_vertex(new_room)
                add_edge(currently_in, exit_direction, new_room)
                reverse = reverse_direction[exit_direction]
                player.travel[reverse]
                # print('resuming from...', player.current_room.id)
                all_explored = False
                return

def bfs(explored_rooms, my_path, all_explored):
    my_path_copy = list(my_path)

    while all_explored:
        rev = my_path_copy.pop()
        rev = reverse_direction[rev]
        my_path.append(rev)
        player.travel(rev)
        currently_in = player.current_room.id
        for exit_direction, exit_room in explored_rooms[currently_in].items():
            if exit_room == '?':
                # print('resuming from...', player.current_room.id)
                all_explored = False
                return

print(my_path)    
bfs(explored_rooms, my_path, all_explored)
while len(explored_rooms) != len(room_graph):
    
    done = dft(explored_rooms, my_path)
    if done and len(explored_rooms) != len(room_graph):
        bfs(explored_rooms, my_path, all_explored)
# dft(explored_rooms, my_path)
# bfs(explored_rooms, my_path, all_explored)
# dft(explored_rooms, my_path)
# bfs(explored_rooms, my_path, all_explored)

print(len(explored_rooms))
print('explored rooms', explored_rooms)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
traversal_path = my_path


for move in traversal_path:
    player.travel(move)
    # print('moving...', move)
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