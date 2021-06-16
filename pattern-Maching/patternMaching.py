from algo1 import *
from hashtable import *
from linkedlist import *
from myarray import *
from mydictionary import *

#======================================================#

        #==========================#
                #Ejercicio1
        #==========================#      
def existChar(string,C):
    #Verifica si Existe un Char especifico en un string
    for element in string:
        if element== C:
            return True
        
    return False
        #==========================#
                #Ejercicio2
        #==========================#
def isPalindrome(string):
    #Verifica si el string es palindromo
    for idx in range(0,len(string)):
        if idx > (len(string)-idx):
            break
        if string[idx]!=string[(len(string)-1)-idx]:
            return False
    
    return True
        #==========================#
                #Ejercicio3
        #==========================#
def mostRepeatedChar(string):
    hash_string= Array(len(string),Dictionary())
    
    for element in string:
        cant_ocurrence= dictSearch(hash_string,element)
        if cant_ocurrence:
            dictUpdate(hash_string,element,cant_ocurrence+1)
        else:
            dictInsert(hash_string,element,1)
    
    char_max_ocurrence= ""
    value=0
    for idx in range(len(hash_string)):
        if hash_string[idx]==None:
            continue
        current= hash_string[idx].head
        
        while current:
            if char_max_ocurrence=="":
                char_max_ocurrence= current.value.key
                value= current.value.value
            if current.value.value > value:
                char_max_ocurrence= current.value.key
                value= current.value.value
            
            current= current.nextNode
    print("[",end="")
    for element in hash_string:        
        if element:
            element= element.head
            print("(",element.value.key,":",str(element.value.value),")",end=",")
        else:
            print("(None)",end=",")
    print("]")
    
    return char_max_ocurrence
        #==========================#
                #Ejercicio4
        #==========================#
def getBiggestIslandLen(String):
    pass

#======================================================#

if __name__ == '__main__':
    
    print("is Palindrome de \"anitalavalatina\"",isPalindrome("anitalavalatina"))
            
    print("el caracter mas repetido en \"aaabcddba\": ",mostRepeatedChar("aaabcddba"))  