from algo1 import *
from graphs import *
from linkedlist import *
from myarray import *

print("=================================================")

vertices= LinkedList()

add(vertices,"1")
add(vertices,"2")
add(vertices,"3")
add(vertices,"4")
add(vertices,"5")
add(vertices,"6")

directAristas= LinkedList()


add(directAristas,"6")
add(directAristas,"4")

add(directAristas,"5")
add(directAristas,"4")

add(directAristas,"4")
add(directAristas,"3")

add(directAristas,"4")
add(directAristas,"2")

add(directAristas,"3")
add(directAristas,"1")

add(directAristas,"2")
add(directAristas,"1")

graphs= noDirectCreateGraph(vertices,directAristas)

aristas= LinkedList()

add(aristas,"6")
add(aristas,"4")

add(aristas,"5")
add(aristas,"4")

add(aristas,"3")
add(aristas,"4")

add(aristas,"4")
add(aristas,"3")

add(aristas,"2")
add(aristas,"4")

add(aristas,"4")
add(aristas,"2")

add(aristas,"1")
add(aristas,"3")

add(aristas,"3")
add(aristas,"1")

add(aristas,"1")
add(aristas,"2")

add(aristas,"2")
add(aristas,"1")

graph= directCreateGraph(vertices,aristas)
print("================================================")
print("             EXIST PATH")

value= existPath(graph,"1","3")
print("exist path in V1 y V3: ",value)

value= existPath(graph,"1","4")

print("exist path in V1 y V4: ",value)

value= existPath(graph,"5","4")

print("exist path in V5 y V4: ",value)

value= existPath(graph,"4","5")

print("exist path in V4 y V5: ",value)

print("================================================")
print("             IS CONNECTED")
value= isConnected(graphs)

print("is connected: ",value)

print("================================================")
print("             IS TREE")
value= isTree(graphs)

print("is tree: ",value)