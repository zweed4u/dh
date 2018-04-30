#!/usr/bin/python3
import json


class Maze:
    def __init__(self):
        self.priority_queue = {
            'S': 0,  # start
            'A': 999,
            'B': 999,
            'C': 999,
            'D': 999,
            'F': 999,
            'G': 999,
            'H': 999,
            'I': 999,
            'J': 999,
            'K': 999,
            'L': 999,
            'E': 999  # end
        }

        self.neighbors = {
            'S': {'A':7, 'B':2, 'C':3},
            'A': {'S':7, 'B':3, 'D':4},
            'B': {'S':2, 'A':3, 'D':4, 'H':1},
            'C': {'S':3, 'L':2},
            'D': {'A':4, 'B':4, 'F':5},
            'F': {'D':5, 'H':3},
            'G': {'H':2, 'E':2},
            'H': {'F':3, 'G':2, 'B':1},
            'I': {'K':4, 'L':4, 'J':6},
            'J': {'L':4, 'I':6, 'K':4},
            'K': {'E':5, 'I':4, 'J':4},
            'L': {'C':2, 'I':4, 'J':4},
            'E': {'G':2, 'K':5}  # end
        }

        self.heuristic_euclidean_distance = {
            'S': 10,  # start
            'A': 9,
            'B': 7,
            'C': 8,
            'D': 8,
            'F': 6,
            'G': 3,
            'H': 6,
            'I': 4,
            'J': 4,
            'K': 3,
            'L': 6,
            'E': 0  # end
        }

    def traverse(self):
        traveled = []
        #print(json.dumps(self.priority_queue, indent=2))
        for neighbor in self.neighbors['S']:
            self.priority_queue[neighbor] = self.neighbors['S'][neighbor]

        # Sort and pop
        for node in self.priority_queue:
            self.priority_queue[node] += self.heuristic_euclidean_distance[node]
        self.priority_queue = dict(sorted(self.priority_queue.items(), key=lambda x: x[1]))
        traveled.append('S')
        self.priority_queue.pop('S', None)
        #print(json.dumps(self.priority_queue, indent=2))

        while self.priority_queue.get('E', None):
            shortest_node = list(self.priority_queue.items())[0][0]
            for neighbor in self.neighbors[shortest_node]:
                # neglect already traveled
                if neighbor in traveled:
                    continue
                # already have smallest path
                if self.neighbors[shortest_node][neighbor] + self.priority_queue[shortest_node] > self.priority_queue[neighbor]:
                    continue
                self.priority_queue[neighbor] = self.neighbors[shortest_node][neighbor] + self.priority_queue[shortest_node]
            
            # Sort and pop
            for node in self.priority_queue:
                self.priority_queue[node] += self.heuristic_euclidean_distance[node]
            self.priority_queue = dict(sorted(self.priority_queue.items(), key=lambda x: x[1]))
            traveled.append(shortest_node)
            self.priority_queue.pop(shortest_node, None)
            #print(json.dumps(self.priority_queue, indent=2))
        
        traveled.reverse()
        prev_node = 'E'
        path = [prev_node]
        for node in traveled:
            if self.neighbors[node].get(prev_node, None) is None:
                pass
            else:
                path.append(node)
                prev_node = node
        path.reverse()
        print(path)


Maze().traverse()
