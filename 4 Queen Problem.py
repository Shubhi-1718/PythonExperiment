adj_list = {
    'A':['B','E','C','D'],
    'B':['F','G'],
    'C':['H'],
    'D':['I'],
    'E':['J','K'],
    'F':[],
    'G':['L'],
    'H':['M'],
    'I':['N'],
    'J':['O'],
    'K':[],
    'L':[],
    'M':['P'],
    'N':['Q'], 
    'O':[],
    'P':[],
    'Q':[]
}
label={
    'A':[0],
    'B':[{'1,1'}],
    'C':[{'1,2'}],
    'D':[{'1,3'}],
    'E':[{'1,4'}],
    'F':[{'1,1'},{'2,3'}],
    'G':[{'1,1'},{'2,4'}],
    'H':[{'1,2'},{'2,4'}],
    'I':[{'1,3'},{'2,1'}],
    'J':[{'1,4'},{'2,1'}],
    'K':[{'1,4'},{'2,2'}],
    'L':[{'1,1'},{'2,4'},{'3,2'}],
    'M':[{'1,2'},{'2,4'},{'3,1'}],
    'N':[{'1,3'},{'2,1'},{'3,4'}],
    'O':[{'1,4'},{'2,1'},{'3,3'}],
    'P':[{'1,2'},{'2,4'},{'3,1'},{'4,3'}],
    'Q':[{'1,3'},{'2,1'},{'3,4'},{'4,2'}]
    
}
traversal_path =[]
stack=[]
visited=[]
goal =['P','Q']
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
traversal_path=DFS(adj_list,'A',traversal_path)
print(traversal_path)
while traversal_path:
    s=traversal_path.pop(0)
    print(label[s])
