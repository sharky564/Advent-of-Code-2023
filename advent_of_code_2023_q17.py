import heapq
import time

class PriorityQueue():
    def __init__(self, data=[]):
        self.heap = list(data)
        self.dict = dict()
        self._heapify()
    
    def __len__(self):
        return len(self.heap)

    def _heapify(self):
        heapq.heapify(self.heap)
        self.dict = dict((elem, pos) for pos, elem in enumerate(self.heap))
        if len(self.heap) != len(self.dict):
            raise ValueError("Duplicate elements in priority queue")
    
    def push(self, element, priority):
        if element in self.dict:
            return False
        position = len(self.heap)
        self.heap.append((priority, element))
        self.dict[element] = position
        self._siftdown(position)
        return True
    
    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty priority queue")
        element = self.heap[0][1]
        del self.dict[element]
        if len(self.heap) == 1:
            self.heap.pop()
            return element
        
        last = self.heap.pop()
        self.heap[0] = last
        self.dict[last[1]] = 0
        pos = self._siftup(0)
        self._siftdown(pos)
        return element
    
    def update(self, element, priority):
        position = self.dict[element]
        self.heap[position] = (priority, element)
        self.dict[element] = position
        position = self._siftup(position)
        self._siftdown(position)
    
    def remove(self, element):
        try:
            position = self.dict[element]
            del self.dict[element]
        except KeyError:
            raise
        if position == len(self.heap) - 1:
            self.heap.pop()
            return
        
        last = self.heap.pop()
        self.heap[position] = last
        self.dict[last[1]] = position
        position = self._siftup(position)
        self._siftdown(position)

    def _siftup(self, position):
        curr_heap, curr_dict = self.heap, self.dict
        element = curr_heap[position]
        end_position = len(curr_heap)
        left_child_position = 2 * position + 1
        while left_child_position < end_position:
            left_child = curr_heap[left_child_position]
            try:
                right_child_position = left_child_position + 1
                right_child = curr_heap[right_child_position]
                if right_child < left_child:
                    curr_heap[position], curr_heap[right_child_position] = right_child, element
                    position, right_child_position = right_child_position, position
                    curr_dict[element[1]], curr_dict[right_child[1]] = position, right_child_position
                else:
                    curr_heap[position], curr_heap[left_child_position] = left_child, element
                    position, left_child_position = left_child_position, position
                    curr_dict[element[1]], curr_dict[left_child[1]] = position, left_child_position
            except IndexError:
                curr_heap[position], curr_heap[left_child_position] = left_child, element
                position, left_child_position = left_child_position, position
                curr_dict[element[1]], curr_dict[left_child[1]] = position, left_child_position
            left_child_position = 2 * position + 1
        return position
    
    def _siftdown(self, position):
        curr_heap, curr_dict = self.heap, self.dict
        element = curr_heap[position]
        while position > 0:
            parent_position = (position - 1) // 2
            parent = curr_heap[parent_position]
            if parent > element:
                curr_heap[position], curr_heap[parent_position] = parent, element
                position, parent_position = parent_position, position
                curr_dict[element[1]], curr_dict[parent[1]] = position, parent_position
            else:
                break
        return position


def get_neighbours1(node, grid):
    # node is a tuple of (x, y, direction)
    # direction is 0, 1 for north-south, east-west
    x, y, direction = node
    neighbours = {}
    if direction != 0:
        dist = 0
        for i in range(1, 4):
            if x - i >= 0:
                dist += grid[x - i][y]
                neighbours[(x - i, y, 0)] = dist
            else:
                break
        dist = 0
        for i in range(1, 4):
            if x + i < len(grid):
                dist += grid[x + i][y]
                if x + i == len(grid) - 1 and y == len(grid[0]) - 1:
                    neighbours[(x + i, y, -1)] = dist
                else:
                    neighbours[(x + i, y, 0)] = dist
            else:
                break
    if direction != 1:
        dist = 0
        for i in range(1, 4):
            if y - i >= 0:
                dist += grid[x][y - i]
                neighbours[(x, y - i, 1)] = dist
            else:
                break
        dist = 0
        for i in range(1, 4):
            if y + i < len(grid[0]):
                dist += grid[x][y + i]
                if x == len(grid) - 1 and y + i == len(grid[0]) - 1:
                    neighbours[(x, y + i, -1)] = dist
                else:
                    neighbours[(x, y + i, 1)] = dist
            else:
                break
    return neighbours


def get_neighbours2(node, grid):
    # node is a tuple of (x, y, direction)
    # direction is 0, 1 for north-south, east-west
    x, y, direction = node
    neighbours = {}
    if direction != 0:
        dist = 0
        for i in range(1, 4):
            if x - i >= 0:
                dist += grid[x - i][y]
        for i in range(4, 11):
            if x - i >= 0:
                dist += grid[x - i][y]
                neighbours[(x - i, y, 0)] = dist
            else:
                break
        dist = 0
        for i in range(1, 4):
            if x + i < len(grid):
                dist += grid[x + i][y]
        for i in range(4, 11):
            if x + i < len(grid):
                dist += grid[x + i][y]
                if x + i == len(grid) - 1 and y == len(grid[0]) - 1:
                    neighbours[(x + i, y, -1)] = dist
                else:
                    neighbours[(x + i, y, 0)] = dist
            else:
                break
    if direction != 1:
        dist = 0
        for i in range(1, 4):
            if y - i >= 0:
                dist += grid[x][y - i]
        for i in range(4, 11):
            if y - i >= 0:
                dist += grid[x][y - i]
                neighbours[(x, y - i, 1)] = dist
            else:
                break
        dist = 0
        for i in range(1, 4):
            if y + i < len(grid[0]):
                dist += grid[x][y + i]
        for i in range(4, 11):
            if y + i < len(grid[0]):
                dist += grid[x][y + i]
                if x == len(grid) - 1 and y + i == len(grid[0]) - 1:
                    neighbours[(x, y + i, -1)] = dist
                else:
                    neighbours[(x, y + i, 1)] = dist
            else:
                break
    return neighbours


def print_path(grid, path):
    curr_x = 0
    curr_y = 0
    for node in path:
        if node[0][0] == curr_x:
            if node[0][1] > curr_y:
                for i in range(curr_y + 1, node[0][1] + 1):
                    grid[curr_x][i] = '>'
            else:
                for i in range(curr_y - 1, node[0][1] - 1, -1):
                    grid[curr_x][i] = '<'
        else:
            if node[0][0] > curr_x:
                for i in range(curr_x + 1, node[0][0] + 1):
                    grid[i][curr_y] = 'v'
            else:
                for i in range(curr_x - 1, node[0][0] - 1, -1):
                    grid[i][curr_y] = '^'
        curr_x = node[0][0]
        curr_y = node[0][1]
    for row in grid:
        print(''.join(map(str, row)))



def part1():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    grid = [list(map(int, x)) for x in out]

    init_node = (0, 0, -1)
    end_node = (len(grid)-1, len(grid[0])-1, -1)
    visited = set()
    visited.add(init_node)
    distances = {init_node: 0}
    minimal_tree = {}
    priority_queue = PriorityQueue()
    priority_queue.push(init_node, 0)
    while priority_queue:
        if end_node in visited:
            path = []
            curr_node = end_node
            while curr_node != init_node:
                path.append((curr_node[:2], distances[curr_node]))
                curr_node = minimal_tree[curr_node]
            path.append((init_node[:2], distances[init_node]))
            path.reverse()
            print(distances[end_node])
            print_path(grid, path)
            return
        
        node = priority_queue.pop()
        visited.add(node)
        neighbours = get_neighbours1(node, grid)
        for neighbour in neighbours:
            if neighbour[:2] == (0, 0):
                continue
            if neighbour not in distances:
                distances[neighbour] = distances[node] + neighbours[neighbour]
                minimal_tree[neighbour] = node
            elif distances[neighbour] > distances[node] + neighbours[neighbour]:
                distances[neighbour] = distances[node] + neighbours[neighbour]
                minimal_tree[neighbour] = node
            if neighbour not in visited:
                try:
                    priority_queue.update(neighbour, distances[neighbour])
                except KeyError:
                    priority_queue.push(neighbour, distances[neighbour])
    print("No path found")


def part2():
    f = open("input.txt", 'r')
    out = f.read().split('\n')
    grid = [list(map(int, x)) for x in out]

    init_node = (0, 0, -1)
    end_node = (len(grid)-1, len(grid[0])-1, -1)
    visited = set()
    visited.add(init_node)
    distances = {init_node: 0}
    minimal_tree = {}
    priority_queue = PriorityQueue()
    priority_queue.push(init_node, 0)
    while priority_queue:
        if end_node in visited:
            path = []
            curr_node = end_node
            while curr_node != init_node:
                path.append((curr_node[:2], distances[curr_node]))
                curr_node = minimal_tree[curr_node]
            path.append((init_node[:2], distances[init_node]))
            path.reverse()
            print(distances[end_node])
            print_path(grid, path)
            return
        
        node = priority_queue.pop()
        visited.add(node)
        neighbours = get_neighbours2(node, grid)
        for neighbour in neighbours:
            if neighbour[:2] == (0, 0):
                continue
            if neighbour not in distances:
                distances[neighbour] = distances[node] + neighbours[neighbour]
                minimal_tree[neighbour] = node
            elif distances[neighbour] > distances[node] + neighbours[neighbour]:
                distances[neighbour] = distances[node] + neighbours[neighbour]
                minimal_tree[neighbour] = node
            if neighbour not in visited:
                try:
                    priority_queue.update(neighbour, distances[neighbour])
                except KeyError:
                    priority_queue.push(neighbour, distances[neighbour])
    print("No path found")
    


start = time.time()
part1()
end = time.time()
print(end - start)

start = time.time()
part2()
end = time.time()
print(end - start)