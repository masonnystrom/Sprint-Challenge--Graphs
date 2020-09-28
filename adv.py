from room import Room
from player import Player
from world import World
import math
from util import Queue, Stack
import random
from ast import literal_eval

reverse_direction = {
                    'n': 's', 
                    's': 'n', 
                    'e': 'w', 
                    'w': 'e'
                    }

class Path:
    """
Graph to represent the map
    1. Tarnslate into graph terminology
    vertex = room
    edge = neighboring rooms
    path = list of directions to take to traverse the map
    no weights

    2. bulid graph
    problem set has map of rooms with various connections 
     traverse the graph
    step 3 with pseudocode:
    tranverse the graph
    If we find a room to go through
        go through and record
        then want to traverse all of its connected rooms
    and market them as visited
    When Path ends, tranverse to nearest room with unexplored rooms. 
    Repeat until all rooms have been explored. 
    return path
    """
    def path_traversal(self, room, visited=None):
        """
        method to recursively traverse the path using reverse directions
        """

        # initialize our visited while is none
        if visited is None:
            visited = set()
            
            # create empty path to add directions
        direction_path = []
            
        visited.add(room.id)

            # get the possible exit/next paths for room
        for exit_path in room.get_exits():
            
            # go into a new room
            next_room = room.get_room_in_direction(exit_path)
            
            if next_room.id not in visited:
                
                # use recursion to visit other rooms
                unvisited_rooms = self.path_traversal(next_room, visited)

                # if there are rooms still unvisted
                if unvisited_rooms:
                    # curr path uses reverse directions of exits to get back to previous rooms
                    currPath = [exit_path] + unvisited_rooms + [reverse_direction[exit_path]]

                # if all rooms have been visited
                else:
                    currPath = [exit_path, reverse_direction[exit_path]]
                
                direction_path = direction_path + currPath
        # return final path
        return direction_path

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = Path().path_traversal(player.current_room)



# TRAVERSAL TEST - DO NOT MODIFY
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
