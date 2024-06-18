from problem import MultiFoodSearchProblem
from fringes import Queue, PriorityQueue, Stack

#MultiFoodSearchProblem:
class MultiSearchStrategy:
    def search(self, g: MultiFoodSearchProblem, src: tuple, dsts: list) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dsts
        return expanded, path
    
    def get_path(self, src : tuple , dst: tuple , parents : dict)-> list : 
        path = []
        x = dst 
        while x != -1 : 
            path.append(x)
            x = parents[x]
        path.reverse()
        return path
    
    def get_directions(self, locations):
        directions = []
        for i in range(1, len(locations)):
            curr = locations[i]
            prev = locations[i-1]
            if curr[0] > prev[0]:
                directions.append("S")
            elif curr[0] < prev[0]:
                directions.append("N")
            elif curr[1] > prev[1]:
                directions.append("E")
            elif curr[1] < prev[1]:
                directions.append("W")
        directions.append("Stop")
        return directions
    
    def __init__(self):
        self.expanded = []
class MultiBFS(MultiSearchStrategy):
    def find_path(self, g: MultiFoodSearchProblem, src: tuple, dst: tuple) -> list:
        q = Queue()
        q.enqueue(src)
        parents = dict()
        parents[src] = -1
        
        while not q.is_empty():
            cur = q.dequeue()
            if cur == dst:
                path = [cur]
                while parents[dst] != -1:
                    path.append(parents[dst])
                    dst = parents[dst]
                path.reverse()
                return path
            successors = g.get_successors(cur)
            for (v, d, w) in successors:
                if v not in parents:
                    parents[v] = cur
                    q.enqueue(v)
        return []
    
    def search(self, g: MultiFoodSearchProblem, src: tuple, dsts: list) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dsts
        if src in dsts:
            path = [src]
            return expanded, path
        
        dsts = dsts.copy()
        dst = dsts.pop(0)
        while dsts:
            next_dst = dsts.pop(0)
            subpath = self.find_path(g, dst, next_dst)
            if not subpath:
                return expanded, [], []
            path += subpath[:-1]
            dst = subpath[-1]
        subpath = self.find_path(g, dst, src)
        if not subpath:
            return expanded, [], []
        path += subpath[:-1]
        path.reverse()
        path.insert(0,src)
        direction = self.get_directions(path)
        
        return expanded, direction, path
                        
class MultiDFS(MultiSearchStrategy):
    def find_path(self, g: MultiFoodSearchProblem, src: tuple, dst: tuple) -> list:
        stack = Stack()
        stack.push(src)
        parents = dict()
        parents[src] = -1
        
        while not stack.is_empty():
            cur = stack.pop()
            if cur == dst:
                path = [cur]
                while parents[dst] != -1:
                    path.append(parents[dst])
                    dst = parents[dst]
                path.reverse()
                return path
            successors = g.get_successors(cur)
            for (v, d, w) in successors:
                if v not in parents:
                    parents[v] = cur
                    stack.push(v)
        return []

    def search(self, g: MultiFoodSearchProblem, src: tuple, dsts: list) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dsts
        if src in dsts:
            path = [src]
            return expanded, path

        dsts = dsts.copy()
        dst = dsts.pop(0)
        while dsts:
            next_dst = dsts.pop(0)
            subpath = self.find_path(g, dst, next_dst)
            if not subpath:
                return expanded, [], []
            path += subpath[:-1]
            dst = subpath[-1]

        subpath = self.find_path(g, dst, src)
        if not subpath:
            return expanded, [], []
        path += subpath[:-1]
        path.reverse()
        path.insert(0,src)
        direction = self.get_directions(path)
        return expanded, direction, path
    
class MultiUCS(MultiSearchStrategy):
    def find_path(self, g: MultiFoodSearchProblem, src: tuple, dst: tuple) -> list:
        pq = PriorityQueue()
        pq.push(src, 0)
        parents = dict()
        parents[src] = -1
        costs = dict()
        costs[src] = 0
        
        while not pq.is_empty():
            cur_cost , cur = pq.dequeue()
            if cur == dst:
                path = [cur]
                while parents[dst] != -1:
                    path.append(parents[dst])
                    dst = parents[dst]
                path.reverse()
                return path
            successors = g.get_successors(cur)
            
            for (v, d, w) in successors:
                new_cost = cur_cost + w
                if v not in costs or new_cost < costs[v]:
                    costs[v] = new_cost
                    parents[v] = cur
                    pq.push(v, new_cost)
        return []

    def search(self, g: MultiFoodSearchProblem, src: tuple, dsts: list) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dsts
        if src in dsts:
            path = [src]
            return expanded, path

        dsts = dsts.copy()
        dst = dsts.pop(0)
        while dsts:
            next_dst = dsts.pop(0)
            subpath = self.find_path(g, dst, next_dst)
            if not subpath:
                return expanded, [], []
            path += subpath[:-1]
            dst = subpath[-1]

        subpath = self.find_path(g, dst, src)
        if not subpath:
            return expanded, [], []
        path += subpath[:-1]
        path.reverse()
        path.insert(0,src)
        direction = self.get_directions(path)
        return expanded, direction, path


       
class MultiAstar(MultiSearchStrategy):
    def find_path(self, g: MultiFoodSearchProblem, src: tuple, dst: tuple) -> list:
        pq = PriorityQueue()
        pq.push(src, 0)
        parents = dict()
        costs = dict()
        parents[src] = -1
        costs[src] = 0

        while not pq.is_empty():
            cost,cur = pq.dequeue()
            if cur == dst:
                path = [cur]
                while parents[dst] != -1:
                    path.append(parents[dst])
                    dst = parents[dst]
                path.reverse()
                return path
            successors = g.get_successors(cur)
            for (v, d, w) in successors:
                if v not in parents:
                    parents[v] = cur
                    costs[v] = costs[cur] + w
                    priority = costs[v] + g.manhattan(v, g.manhattan())
                    pq.push(v, priority)
                    self.expanded.append(v)
        return []

    def search(self, g: MultiFoodSearchProblem, src: tuple, dsts: list) -> tuple:
        path = []
        if src in dsts:
            path = [src]
            return self.expanded, path

        dsts = dsts.copy()
        dst = dsts.pop(0)
        while dsts:
            next_dst = dsts.pop(0)
            subpath = self.find_path(g, dst, next_dst)
            if not subpath:
                return self.expanded, [], []
            path += subpath[:-1]
            dst = subpath[-1]

        subpath = self.find_path(g, dst, src)
        if not subpath:
            return self.expanded, [], []
        path += subpath[:-1]
        path.reverse()
        path.insert(0,src)
        direction = self.get_directions(path)
        return self.expanded, direction, path
        
multi_pacman = MultiFoodSearchProblem("pacman_multi01.txt")

multibfs  = MultiBFS()
multidfs = MultiDFS()
multiucs = MultiUCS()
multiastar = MultiAstar()

expanded, direciton, path = multiucs.search(multi_pacman, multi_pacman.get_start_state(), multi_pacman.get_goal_states())
multi_pacman.animate(direciton)  