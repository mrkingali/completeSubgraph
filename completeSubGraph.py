import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations 

   
node=[]
CompleteSubGraphs=[]


class GraphVisualization:
   
    def __init__(self):
        self.visual = []
          
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def getEdgeList(self,a):
        for i in a:
            self.visual.append(i)
    
    def visualize(self,message):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        message=message+" "+str(self.visual)
        plt.title(message)
        plt.show()

        
## get input of edge and set node list and inputgraph list
"""
            simple input:
            1 2
            2 3
            1 3
            1 4
            END
"""
def getListOfEdgeGraph():
    print("enter enge num like \"0 1\" at the end enter \"END\"")
    edgelist=[]
    input1=input()
    
    while input1!="END":
        
        z=list(map(int,input1.split(" ")))
        if z[0] not in node:
            node.append(z[0])
        if z[1] not in node:
            node.append(z[1])
        edgelist.append(z)
        input1=input()
    E=GraphVisualization()
    E.getEdgeList(edgelist)
    
    E.visualize("input graph ")
    return edgelist

# recursive function for found all subgraph 
# then if they were complete add them to completeSubGraph
def chekNodeContainAllEdge(numberNode1,edges,node1,allnode):
    if numberNode1==0:
        x=True
        for i in range(len(node1)-1):
            for j in range(i+1,len(node1)):
                if ([node1[i],node1[j]] in edges ) or ([node1[j],node1[i]]  in edges):
                    pass
                else: 
                    x=False
        if x==True:
            z=[]
            for i in range(len(node1)-1):
                for j in range(i+1,len(node1)):
                    a=[node1[i],node1[j]]
                    a.sort()
                    z.append(a) 
            z.sort()
            if z not in CompleteSubGraphs:
                if z!=[]:
                    CompleteSubGraphs.append(z)  
    else:
        for i in range(len(allnode)):
            l=node1[:]
            allnode2=allnode[:]
            l.append(allnode[i])
            del allnode2[i]
            chekNodeContainAllEdge(numberNode1-1,edges,l,allnode2)


def foundCompleteSubgraph(graph):
    numberNode=len(node)
    for i in range(numberNode,0,-1):
        chekNodeContainAllEdge(i,graph,[],node)

#get graph from input 
graph=getListOfEdgeGraph()

#extract all of complete subgraph
foundCompleteSubgraph(graph)

# print matrix of subgraph which exist in graphs
count=1
for subgraph in CompleteSubGraphs:
    print (count ,"th subgraph \n")
    l=[]
    for i in range(len(node)):
        l.append([])
        for j in range(len(node)):
            l[i].append(0)

    
    for edge in subgraph:
        
        l[edge[0]-1][edge[1]-1]=1
        l[edge[1]-1][edge[0]-1]=1
        
    for i in range(len(node)):
        print(l[i])
    print("\n")
    count+=1   

#show all of complete subgraph
for subgraph in CompleteSubGraphs:
    Z= GraphVisualization()
    Z.getEdgeList(subgraph)
    index=CompleteSubGraphs.index(subgraph)
    message=str(CompleteSubGraphs.index(subgraph))+"th subgraph : "
    Z.visualize(message)
    