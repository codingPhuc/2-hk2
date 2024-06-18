import sys
import time
import os
import math
class SingleFoodSearchProblem:
    def __init__(self, maze_file):
        self.maze = self.read_maze(maze_file)
        self.start_state = self.get_start_state()
        self.goal_state = self.get_goal_state()
        
    def read_maze(self, maze_file):# reading the maze file 
        with open(maze_file, 'r') as f:
            maze = [line.strip() for line in f]
        return maze
    
    def get_start_state(self):# the beginning state that pacman start at 
        for i in range(len(self.maze)):
            if 'P' in self.maze[i]:
                return (i, self.maze[i].index('P'))
        return None
    
    def get_goal_state(self): # the goal that pack man is trying to get 
        for i in range(len(self.maze)):
            if '.' in self.maze[i]:
                return (i, self.maze[i].index('.'))
        return None
    
    def get_successors(self, state):
        successors = []
        x, y = state
        if x > 0 and self.maze[x-1][y] != '%':
            successors.append(((x-1, y),'N', 1))
        if x < len(self.maze) - 1 and self.maze[x+1][y] != '%':
            successors.append(((x+1, y),'S', 1))
        if y > 0 and self.maze[x][y-1] != '%':
            successors.append(((x, y-1),'W', 1))
        if y < len(self.maze[0]) - 1 and self.maze[x][y+1] != '%':
            successors.append(((x, y+1),'E', 1))   
        return successors
    
    
    def is_goal_state(self, state):# check if it is the goal state 
        return state == self.goal_state
    
    def get_path_cost(self, cost_so_far, current_state, action, next_state):
        return cost_so_far + 1
    
    def print_maze(self):
        for line in self.maze:
            print(line)
    def Tranlate_action(self, state, action):
        i, j = state
        if action == 'N':
            return (i-1, j)
        elif action == 'S':
            return (i+1, j)
        elif action == 'W':
            return (i, j-1)
        elif action == 'E':
            return (i, j+1)
        elif action == 'Stop':
            return (i, j)
        else:
            raise ValueError(f'Unknown action {action}')

    def animate(self, direction):
        current_state = self.start_state
        
        actions = []
        now = self.get_start_state() 
        for i in direction : 
            next = self.Tranlate_action(now,i)
            actions.append(next)
            now= next 
        while actions:
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(len(self.maze)):
                line = ''
                for j in range(len(self.maze[i])):
                    if (i, j) == current_state:
                        line += 'P'
                    elif (i, j) == self.goal_state:
                        line += '.'
                    else:
                        line += self.maze[i][j]
                print(line)
            print('Press Enter to continue...')
            input()
            next_state = actions.pop(0)
            current_state = next_state
   
    def manhattan(self, state1, state2):
        x1, y1 = state1
        x2, y2 = state2
        return abs(x1 - x2) + abs(y1 - y2)

    def euclidean(self, state1, state2):
        x1, y1 = state1
        x2, y2 = state2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
###############################################################################################################################################
class MultiFoodSearchProblem:

    def __init__(self, maze_file):
        self.maze = self.read_maze(maze_file)
        self.start_state = self.get_start_state()
        self.goal_states = self.get_goal_states()
        self.expanded = []
        
    def read_maze(self, maze_file):# reading the maze file 
        with open(maze_file, 'r') as f:
            maze = [line.strip() for line in f]
        return maze
    
    def get_start_state(self):# the beginning state that pacman start at 
        for i in range(len(self.maze)):
            if 'P' in self.maze[i]:
                return (i, self.maze[i].index('P'))
        return None
    
    def get_goal_states(self): # the goals that Pacman is trying to get 
        goal_states = []
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == '.':
                    goal_states.append((i, j))
        return goal_states
    
    def get_successors(self, state):
        successors = []
        x, y= state

        # Check north
        if x > 0 and self.maze[x - 1][y] != '%':
            next_pos = (x - 1, y)
            successors.append((next_pos, 'N', 1))

        # Check south
        if x < len(self.maze) - 1 and self.maze[x + 1][y] != '%':
            next_pos = (x + 1, y)
            successors.append((next_pos, 'S', 1))

        # Check west
        if y > 0 and self.maze[x][y - 1] != '%':
            next_pos = (x, y - 1)
            successors.append((next_pos, 'W', 1))

        # Check east
        if y < len(self.maze[0]) - 1 and self.maze[x][y + 1] != '%':
            next_pos = (x, y + 1)
            successors.append((next_pos, 'E', 1))

        return successors
    
    
    def is_goal_state(self, state):# check if it is a goal state 
        return state in self.goal_states
    
    def get_path_cost(self, cost_so_far, current_state, action, next_state):
        return cost_so_far + 1
    
    def print_maze(self):
        for line in self.maze:
            print(line)
            
    def translate_action(self, state, action):
        # if action == 'Stop':
        #     return state
        # elif action in ('N', 'S', 'W', 'E'):
        #     i, j = state
        #     if action == 'N':
        #         return (i - 1, j)
        #     elif action == 'S':
        #         return (i + 1, j)
        #     elif action == 'W':
        #         return (i, j - 1)
        #     elif action == 'E':
        #         return (i, j + 1)
        i, j = state
        if action == 'N':
            return (i-1, j)
        elif action == 'S':
            return (i+1, j)
        elif action == 'W':
            return (i, j-1)
        elif action == 'E':
            return (i, j+1)
        elif action == 'Stop':
            return (i, j)
        else:
            raise ValueError(f'Unknown action {action}')

    def animate(self, directions):
        current_state = self.start_state
        
        actions = []
        now = self.get_start_state() 
        # for direction in directions: 
        #     for i in direction:
        #         next_state = self.translate_action(now, i)
        #         actions.append(next_state)
        #         now = next_state
        #     actions.append('Stop')
        # print(actions)
        # print(directions)
        # while actions:
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     for i in range(len(self.maze)):
        #         line = ''
        #         for j in range(len(self.maze[i])):
        #             if (i, j) == current_state:
        #                 line += 'P'
        #             elif (i, j) in self.goal_states:
        #                 line += '.'
        #             else:
        #                 line += self.maze[i][j]
        #         print(line)
        #     print('Press Enter to continue...')
        #     input()
        #     next_state = actions.pop(0)
        #     current_state = next_state
        now = self.get_start_state() 
        for i in directions : 
            next = self.translate_action(now,i)
            actions.append(next)
            now= next 
        print(self.get_start_state() )
        # print(actions)
        # print(directions)
        while actions:
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range(len(self.maze)):
                line = ''
                for j in range(len(self.maze[i])):
                    if (i, j) == current_state:
                        line += 'P'
                    elif (i, j) == self.goal_states:
                        line += '.'
                    else:
                        line += self.maze[i][j]
                print(line)
            print('Press Enter to continue...')
            input()
            next_state = actions.pop(0)
            current_state = next_state

    def get_actions(self, start_state, end_state):
        actions = []
        current_state = start_state
        while current_state != end_state:
            for successor, action, _ in self.get_successors(current_state):
                if successor == end_state:
                    actions.append(action)
                    return actions
            for successor, action, _ in self.get_successors(current_state):
                if successor not in actions:
                    actions.append(action)
                    current_state = successor
                    break
        return actions
    
    def get_goals_reached(self, state, goals_reached):
        for food in self.foods:
            if state.is_food_eaten(food) and food not in goals_reached:
                goals_reached.append(food)
        return goals_reached
    
    def heuristic(state):
        pos, food = state
        remaining_food = food.asList()
        total_distance = 0
        for f in remaining_food:
            total_distance += abs(pos[0] - f[0]) + abs(pos[1] - f[1])
        return total_distance
if __name__ == '__main__':
    pacman = SingleFoodSearchProblem("input.txt")
    print(pacman.maze)
    