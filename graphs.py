from algo1 import *
from linkedlist import *
from myarray import *
from mydictionary import *
from myqueue import *

class DirectGraphNode:
    valueVertex= None
    startingVertex= None
    arrivalVertex= None
    
class NoDirectGraphNode:
    parent= None
    distanceOrigin= None
    color= "WHITE"
    valueVertex= None
    startingVertex= None
    
#=========================================#
                 #BFS 
#=========================================#
def BFS(graphs,parentVertex):
    vertexIdx= hash_Key(parentVertex,len(graphs))
    graphs[vertexIdx].distanceOrigin= 0
    graphs[vertexIdx].color= "GREY"
    
    queue= LinkedList()
    
    enqueue(queue,parentVertex)
    
    while queue.head:
        element= dequeue(queue)
        mainVertexIdx= hash_Key(element,len(graphs))
        list_of_adjacent= graphs[mainVertexIdx].startingVertex.head
        while list_of_adjacent:
            vertexIdx= hash_Key(list_of_adjacent.value,len(graphs))
            if graphs[vertexIdx].color == "WHITE":
                graphs[vertexIdx].color= "GREY"
                graphs[vertexIdx].distanceOrigin= graphs[mainVertexIdx].distanceOrigin + 1
                graphs[vertexIdx].parent= graphs[mainVertexIdx].valueVertex
                enqueue(queue,graphs[vertexIdx].valueVertex)
            list_of_adjacent= list_of_adjacent.nextNode
            
        graphs[mainVertexIdx].color= "BLACK"
#=========================================#
        #CREATE GRAPH NO DIRECCIONADOS
#=========================================#
def noDirectCreateGraph(vertexList,edgesList):
    
    graphs= Array(Llength(vertexList),NoDirectGraphNode())
    
    vertex= vertexList.head
    while vertex:
        vertex_index= hash_Key(vertex.value,Llength(vertexList))
        nodeInsert= NoDirectGraphNode()
        nodeInsert.startingVertex= LinkedList()
        nodeInsert.valueVertex= vertex.value
        graphs[vertex_index]= nodeInsert
        
        vertex= vertex.nextNode 
        
    
    adges= edgesList.head
    par= 0
    while adges:
        if par==1:
            arrivalIdx= hash_Key(adges.value,Llength(vertexList))
            #inserta los nodos en sus respectivos lugares ya que es directo
            
            starting_vertex=graphs[stardingIdx].startingVertex
            add(starting_vertex,graphs[arrivalIdx].valueVertex)
            
            arrival_vertex= graphs[arrivalIdx].startingVertex
            add(arrival_vertex,graphs[stardingIdx].valueVertex)
            par= 0
            
        else:
            stardingIdx= hash_Key(adges.value,Llength(vertexList))
            par += 1
        
        adges= adges.nextNode

    return graphs
#=========================================#
        #CREATE GRAPH DIRECCIONADOS
#=========================================#

def directCreateGraph(vertexList,edgesList):
    
    graphs= Array(Llength(vertexList),DirectGraphNode())
    
    vertex= vertexList.head
    
    while vertex:
        vertex_index= hash_Key(vertex.value,Llength(vertexList))
        nodeInsert= DirectGraphNode()
        nodeInsert.startingVertex= LinkedList()
        nodeInsert.arrivalVertex= LinkedList()
        nodeInsert.valueVertex= vertex.value
        graphs[vertex_index]= nodeInsert
        
        vertex= vertex.nextNode
    
    
    adges= edgesList.head
    """
    print("[",end="")
    uwu=adges
    par=0
    while uwu:
        if par==0:
            print("(",uwu.value,sep="",end=",")
            par +=1
        else:
            print(uwu.value, end=");")
            par=0
        uwu=uwu.nextNode
    print("]")
    
    
    
   
    
    print("================================================")
    print("PRINT GRAPHS")
    print("[",end="")
    for element in graphs:
        print(element.valueVertex, end=",")
        current= element.startingVertex.head
        print("(", end="")
        while current:
            print(current.value, end=",")
            current= current.nextNode
        print(")")
    print("]")
    print("================================================")
        
     """   
        
    par= 0
    while adges:
        
        if par==1:            
            arrivalIdx= hash_Key(adges.value,Llength(vertexList))
            #inserta en el nodo de partida los nodos que apunta
            
            starting_vertex=graphs[stardingIdx].startingVertex
            """
            print("[",end="")
            print("SV:",graphs[stardingIdx].valueVertex,end=",",sep="")
            print("AV:",graphs[arrivalIdx].valueVertex,end="]")
            print("")
            
            """
            add(starting_vertex,graphs[arrivalIdx].valueVertex)
            #inserta en el nodo de llegada los nodos que lo apuntan
            arrival_vertex= graphs[arrivalIdx].arrivalVertex
            add(arrival_vertex,graphs[stardingIdx].valueVertex)
            par= 0
        else:
            stardingIdx= hash_Key(adges.value,Llength(vertexList))
            par += 1
        
        adges= adges.nextNode
   
    
    """
    
    print("================================================")
    print("PRINT GRAPHS")
    print("[",end="")
    for element in graphs:
        print(element.valueVertex, end=";")
        current= element.startingVertex.head
        print("(", end="")
        while current:
            print(current.value, end=",")
            current= current.nextNode
        print(");",end="")
        
        
        current= element.arrivalVertex.head
        print("(", end="")
        while current:
            print(current.value, end=",")
            current= current.nextNode
        print(")")
    print("]")
    print("================================================")
    
    """
    
    return graphs

    
    
#=========================================#
                #EXIST PATH
#=========================================#
def existPath(graph,v1,v2):
    
    idx= hash_Key(v1,len(graph))
    
    if not idx:
        return None
    
    adges= graph[idx].startingVertex.head
    
    while adges:
        if adges.value== v2:
            return True

        adges=adges.nextNode
        
    return False

#=========================================#
                #ES CONEXO
#=========================================#

def isConnected(graphs):

    BFS(graphs,graphs[0].valueVertex)
   
    for element in graphs:
        if element.color =="WHITE":
            return False 
          
    return True

#=========================================#
                #ES TREE
#=========================================#
def isTree(graphs):
    
    testGraphs= graphs
    
    for element in testGraphs:
        element.color= "WHITE"
    
    testGraphs[0].color= "GREY"
    value= testGraphs[0].valueVertex   
        
    queue= LinkedList()
    
    enqueue(queue,value)
    
    while queue.head:
        element= dequeue(queue)
        mainVertexIdx= hash_Key(element,len(testGraphs))
        list_of_adjacent= testGraphs[mainVertexIdx].startingVertex.head
        while list_of_adjacent:
            vertexIdx= hash_Key(list_of_adjacent.value,len(testGraphs))
            if testGraphs[vertexIdx]=="GREY":
                return False
            if testGraphs[vertexIdx].color== "WHITE":
                testGraphs[vertexIdx].color= "GREY"
                enqueue(queue,testGraphs[vertexIdx].valueVertex)
            list_of_adjacent= list_of_adjacent.nextNode
        graphs[mainVertexIdx].color= "BLACK"    
    return True


"""
    vertexIdx= hash_Key(parentVertex,len(graphs))
    graphs[vertexIdx].distanceOrigin= 0
    graphs[vertexIdx].color= "GREY"
    
    queue= LinkedList()
    
    enqueue(queue,parentVertex)
    
    while queue.head:
        element= dequeue(queue)
        mainVertexIdx= hash_Key(element,len(graphs))
        list_of_adjacent= graphs[mainVertexIdx].startingVertex.head
        while list_of_adjacent:
            vertexIdx= hash_Key(list_of_adjacent.value,len(graphs))
            if graphs[vertexIdx].color == "WHITE":
                graphs[vertexIdx].color= "GREY"
                graphs[vertexIdx].distanceOrigin= graphs[mainVertexIdx].distanceOrigin + 1
                graphs[vertexIdx].parent= graphs[mainVertexIdx].valueVertex
                enqueue(queue,graphs[vertexIdx].valueVertex)
            list_of_adjacent= list_of_adjacent.nextNode
            
        graphs[mainVertexIdx].color= "BLACK"
"""