from algo1 import *
from graphs import *
from linkedlist import *
from myarray import *

class GraphNode:
    valueVertex= None
    startingVertex= None
    arrivalVertex= None

print("Hola")

T= Array(5,GraphNode())

print(T)

for idx in range(0,len(T)):
    insertando= GraphNode()
    insertando.valueVertex= idx*10
    T[idx]=insertando
    
print("[",sep="",end="")
for element in T:
    element.startingVertex= LinkedList()
    print(element.startingVertex,end=",")
print("]")

