graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['E','F'],
    'D':['G','B'],
    'E':['B','C'],
    'F':['C','H'],
    'G':['I'],
    'H':['K'],
    'I':['J'],
    'J':[],
    'K':['L'],
    'L':['M'],
    'M':['N'],
    'N':[] 
}
label={'A':[0,0],
       'B':[0,3],
       'C':[4,0],
       'D':[3,0],
       'E':[4,3],
       'F':[1,3],
       'G':[3,3],
       'H':[1,0],
       'I':[4,2],
       'J':[0,2],
       'K':[0,1],
       'L':[4,1],
       'M':[2,3],
       'N':[2,0]
       }
visited=[]
queue =[]
goal=['J','N']
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s, end=" ")
        print(label[s],end=" ")
        if s in goal:
            return 
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited,graph,'A')
