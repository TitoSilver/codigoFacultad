from linkedlist import *
from algo1 import *

#===================================================#

def enqueue(Q,element):

  add(Q,element)

  return

#===================================================#
#===================================================#
def dequeue(Q):

  currentNode=Q.head

  if currentNode==None:
    return None #Devuelve None si la Lista esta vacia
  elif currentNode.nextNode==None:
    value= currentNode.value
    Q.head=currentNode.nextNode
    
    return value  #Elimina el elemento si solo se encuentra 1 en la lista

  while currentNode!=None:
    if currentNode.nextNode.nextNode==None:
      value=currentNode.nextNode.value

      currentNode.nextNode=currentNode.nextNode.nextNode
      return value  #Elimina el ultimo elemento

    currentNode= currentNode.nextNode

#===================================================#