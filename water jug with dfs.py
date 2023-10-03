adj_list = {
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

traversal_path =[]
stack=[]
visited=[]
goal =['J','N']

def DFS(adj_list,start,path):
    stack.append(start)
    while stack:
        s=stack.pop()
        path.append(s)
        visited.append(s)
        if s in goal:
            return path
        for neighbour in adj_list[s]:
            if neighbour not in visited:
                stack.append(neighbour)
DFS(adj_list,'A',traversal_path)
print(traversal_path)
while traversal_path:
    s=traversal_path.pop(0)
    print(label[s],end=" ")
