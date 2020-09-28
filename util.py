# util class


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

#from util import Stack, Queue  # These may come in handy
from collections import deque


# Failed attempt 1

# class MapGraph:
    
#     def __init__(self):
#         self.vertices = room_graph

#     def get_neighbors(self, room_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         return self.vertices[room_id][1] 

# def dft(starting_room):
#     # initialize graph
#     graph = MapGraph()
#     room_stack = Stack()
#     direction_stack = Stack()
    
#     # initialize empty path 
#     path = []    
    
#     # initialize empty set to store vistied rooms
#     visited = set()
    
#     room_stack.push(starting_room)

#     # while room_stack is not empty
#     while room_stack.size() > 0:
#         # pop the first room and direction
#         currRoom = room_stack.pop()
#         currDir = direction_stack.pop()
        
#         # append direction to path
#         path.append(currDir)
        
#         if currRoom not in visited:
#             # record the room
#             visited.add(currRoom)
            
#             # check to see if it contains more rooms to explore ("?")
#             edges = graph.get_neighbors(currRoom)
            
#             for direction in edges.keys():
#                 direction_stack.push(direction)
            
#             for room in edges.values():
#                 room_stack.push(room)
#     return [path, visited]