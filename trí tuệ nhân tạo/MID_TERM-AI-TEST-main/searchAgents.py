from problem import SingleFoodSearchProblem, MultiFoodSearchProblem
from fringes import Queue, PriorityQueue, Stack

#SingleFoodSearchProblem:
class SearchStrategy:
    def search(self, g: SingleFoodSearchProblem, src: tuple, dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
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
    
    def get_priority(self, queue, vertex):
        for item in queue:
            if item[1] == vertex:
                return item[0]
        return None
    
class BFS(SearchStrategy):
    def search(self, g: SingleFoodSearchProblem, src: tuple , dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        if src == dst : 
            expanded = []
            path = [src]
            return expanded , path 
        q= Queue()
        q.enqueue(src)
        expanded =[]
        parents = dict()
        parents[src] = -1 
        
        while not q.is_empty() : 
            cur = q.dequeue()
            expanded.append(cur)
            successors = g.get_successors(cur) 
            for(v,d ,w) in  successors : 
                if v not in expanded and not q.contain(v):
                    if v == dst : 
                        parents[v] = cur 
                        path = self.get_path(src ,dst,parents)
                        direction =  self.get_directions(path)
                        return direction ,path
                    parents[v] = cur 
                    q.enqueue(v)

class UCS(SearchStrategy):
    def search(self, g: SingleFoodSearchProblem, src: tuple, dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        if src == dst:
            expanded = []
            path = [src]
            return expanded, path
        pq = PriorityQueue()
        pq.push(src, 0)
        expanded = []
        parents = dict()
        parents[src] = -1
        g_score = dict()
        g_score[src] = 0

        while not pq.is_empty():
            cur = pq.dequeue()[1]
            expanded.append(cur)
            if cur == dst:
                path = self.get_path(src, dst, parents)
                direction = self.get_directions(path)
                return direction, path
            successors = g.get_successors(cur)
            for (v, d, w) in successors:
                if v not in expanded:
                    new_g_score = g_score[cur] + w
                    if v not in g_score or new_g_score < g_score[v]:
                        parents[v] = cur
                        g_score[v] = new_g_score
                        priority = new_g_score
                        if pq.contain(v):
                            pq.items.remove((self.get_priority(pq.items, v), v))
                        pq.push(v, priority)
        return [], []
   

class DFS(SearchStrategy):
    def search(self, g: SingleFoodSearchProblem, src: tuple , dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        if src == dst : 
            expanded = []
            path = [src]
            return self.get_directions(path)
        q= Stack()
        q.push(src)
        expanded =[]
        parents = dict()
        parents[src] = -1 
        
        while not q.is_empty() : 
            cur = q.pop()
            expanded.append(cur)
            successors = g.get_successors(cur) 
            for(v, d, w) in  successors : 
                if v not in expanded and not q.contain(v):
                    if v == dst : 
                        parents[v] = cur 
                        path = self.get_path(src ,dst,parents)
                        direction =  self.get_directions(path)
                        return direction ,path
                    parents[v] = cur 
                    q.push(v)           

class Astar(SearchStrategy):
    def search(self, g: SingleFoodSearchProblem, src: tuple, dst: tuple) -> tuple:
        expanded = [] # list of expanded vertices in the traversal order
        path = [] # path from src to dst
        if src == dst:
            expanded = []
            path = [src]
            return expanded, path
        pq = PriorityQueue()
        pq.push(src, 0)
        expanded = []
        parents = dict()
        parents[src] = -1
        g_score = dict()
        g_score[src] = 0
        f_score = dict()
        f_score[src] = g.manhattan(src, dst)
        while not pq.is_empty():
            cur = pq.dequeue()[1]
            expanded.append(cur)
            if cur == dst:
                path = self.get_path(src, dst, parents)
                direction = self.get_directions(path)
                return direction, path
            successors = g.get_successors(cur)
            for (v, d, w) in successors:
                new_g_score = g_score[cur] + w
                if v not in g_score or new_g_score < g_score[v]:
                    parents[v] = cur
                    g_score[v] = new_g_score
                    f_score[v] = g_score[v] + g.manhattan(v, dst)
                    priority = f_score[v]
                    if pq.contain(v):
                        pq.items.remove((self.get_priority(pq.items, v), v))
                    pq.push(v, priority)
        return [], []
    

pac_man = SingleFoodSearchProblem("pacman_single01.txt")
bfs  = BFS()
dfs = DFS()
usc = UCS()
astar = Astar()

heuristic1 = pac_man.manhattan # heuristic 1
heuristic2 = pac_man.euclidean # heuristic 2

direciton, path = astar.search(pac_man, pac_man.get_start_state(), pac_man.get_goal_state())
actions = []
now = pac_man.get_start_state() 
for i in direciton : 
    next = pac_man.Tranlate_action(now,i)
    actions.append(next)
    now= next

#print(actions) 
# pac_man.animate(direciton)  
# direciton ,path=  usc.search(pac_man, pac_man.get_start_state(), pac_man.get_goal_state())
# pac_man.animate(direciton)
direciton, path = usc.search(pac_man, pac_man.get_start_state(), pac_man.get_goal_state())
pac_man.animate(direciton)
# print(direciton)
# Print out the value of heuristic 1 (manhattan) at the start position and the destination position.
print("Heuristic 1:", heuristic1(pac_man.get_start_state(), pac_man.get_goal_state()))
# Print out the value of heuristic 2 (euclidean) at the start position and the destination position.
print("Heuristic 2:", heuristic2(pac_man.get_start_state(), pac_man.get_goal_state()))













