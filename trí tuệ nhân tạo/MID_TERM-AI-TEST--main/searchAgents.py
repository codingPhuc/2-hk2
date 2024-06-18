from problem import SingleFoodSearchProblem 
from fringes import Queue 
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
            

pac_man = SingleFoodSearchProblem("pacman_single01.txt")
bfs  = BFS()

print(bfs)
destination = (pac_man.get_goal_state(),"Stop")
start = ( pac_man.get_start_state(),"Stop")
print(pac_man.get_start_state())
expanded, path = bfs.search(pac_man, pac_man.get_start_state(), pac_man.get_goal_state())
print(path)
print(expanded)
actions = [(3, 11), (3, 12), (3, 13), (4, 13), (5, 13), (5, 12), (6, 12), (7, 12), (7, 11), (7, 10), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1)]
pac_man.animate(actions)