class Search:

    # TREE Breadth First Search BY Graph Search
    def treeBreadthFirstSearch(self, problem, initial_state, goal_state):
        frontier = [initial_state]
        if not frontier:
            raise Exception("Empty Frontier")
        if initial_state == goal_state:
            return initial_state
        
        for key in problem:
            children = problem.get(key)
            for child in children:
                if child not in visited:
                    if child == goal_state:
                        return child
                    print('expanded', child)
                    frontier.insert(0, child)
    
    # GRAPH Breadth First Search BY Graph Search
    def graphBreadthFirstSearch(self, problem, initial_state, goal_state):
        frontier = [initial_state]
        visited = []
        if not frontier:
            raise Exception("Empty Frontier")
        if initial_state == goal_state:
            return initial_state
        
        for key in problem:
            children = problem.get(key)
            visited.append(key)

            for child in children:
                if child not in visited:
                    print('expanded', child)
                    if child == goal_state:
                        return child
                    frontier.insert(0, child)

    # TREE Depth first search
    def treeDepthFirstSearch(self, graph,start,goal,stack):
        stack.append(start)
        print('The path traversed is:')

        while stack:
            # Pop from stack to set current element
            element=stack.pop()
            print(element)
            if(element==goal):
                break
            for neighbor in graph[element]:
                stack.append(neighbor)

    # GRAPH Depth first search
    def graphDepthFirstSearch(self, graph,start,goal,stack,visited):
        stack.append(start)
        visited.append(start)
        print('The path traversed is:')

        while stack:
            # Pop from stack to set current element
            element=stack.pop()
            print(element)
            if(element==goal):
                print(visited)
                break
            for neighbor in graph[element]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.append(neighbor)


    def uniformCostSearch(self, problem=[], initial_state=None, goal_state=None):

        current_state = {
            "node": initial_state,
            "cost": 0,
        }

        frontier = [initial_state]
        # print(problem)
        explored = [];

        if not frontier: 
            return 'Not Found'

# Depth First Search
graphProblem = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "G"],
    "D": ["G"],
    "G": []
}


problem = [
    {
        "node": "S",
        "h": 7,
        "children":  [
            { "node": 'A', "h": 5, "cost" : 3 },
            { "node": "B", 'h': 7, "cost": 1},
        ],
    },
    {
        "node": "A",
        "h": 5,
        "children":  [
            { "node": "B", 'h': 7, "cost": 2},
            { "node": "C", 'h': 4, "cost": 2},
        ]
    },
    {
        "node": "B",
        "h": 7,
        "children":  [
            { "node": "C", 'h': 4, "cost": 3},
        ]
    },
    {
        "node": "C",
        "h": 4,
        "children":  [
            { "node": "D", 'h': 1, "cost": 3},
            { "node": "G", 'h': 0, "cost": 3},
        ]
    },
    {
        "node": "D",
        "h": 1,
        "children":  [
            { "node": "G", 'h': 0, "cost": 1},
        ]
    },
    {
        "node": "G",
        "h": 0,
        "children":  []
    }
]

search = Search()

visited = [] # Set to keep track of visited nodes.

print(graphProblem)

# Depth First Search
print('TREE BREADTH FIRST SEARCH')
search.treeBreadthFirstSearch(graphProblem, 'S', 'G')

print('GRAPH BREADTH FIRST SEARCH')
search.graphBreadthFirstSearch(graphProblem, 'S', 'G')

print('TREE DEPTH FIRST SEARCH')
search.treeDepthFirstSearch(graphProblem, 'S', 'G', [])

print('GRAPH DEPTH FIRST SEARCH')
search.graphDepthFirstSearch(graphProblem, 'S', 'G', [], visited)

