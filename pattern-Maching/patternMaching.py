from algo1 import *
from hashtable import *
from linkedlist import *
from myarray import *
from mydictionary import *

#======================================================#
#======================================================#
#funciones universales
#crea una tabla hash con los elementos comprimidos:


#======================================================#
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
def getBiggestIslandLen(string):

    hash_string = Array(len(string),Dictionary())
    preview_element=""
    count= 0
    for element in string:
        if preview_element=="":
            preview_element= element
            count = 1
        elif element== preview_element:
            count += 1
        else:
            dictInsert(hash_string,preview_element,count)
            preview_element= element
            count= 1
    
    if string[len(string)-1]== string[len(string)-2]:
        dictInsert(hash_string,preview_element,count)

    print("PRINT HASHTABLE")
    print("[",end="")
    for element in hash_string:
        if element:
            print("(",element.head.value.key,":",element.head.value.value,end="),")
        else:
            print("( NONE )",end=",")
    print("]")

    max_count=0
    max_element=""
    for element in hash_string:
        if element:
            element=element.head
            while element:
                if max_element=="":
                    max_element=element.value.key
                    max_count=element.value.value
                elif element.value.value > max_count:
                    max_element=element.value.key
                    max_count=element.value.value
                element= element.nextNode

    print("max_element: ",max_element, "==> max_count: ",max_count)

    return max_count
        #==========================#
                #Ejercicio5
        #==========================#
def isAnagram(string, subString):

    pass
        #==========================#
                #Ejercicio6
        #==========================#
def verifyBalancedParentheses(string):
    hash_table=Array(2,Dictionary() )

    """
    #En este codigo voy a tomar dos valores posibles:
    si es "(" suma 1 al contador, si es ")" resta 1 al contador
    si es "*" no hace nada 

    como la tabla hash solo tiene dos valores, el contador de par de parentesis y letra aleatorio, va a recorrer el string
    una unica vez, si en algun momento el contador de par de parentesis <0 el ciclo se detiene y se da como falso
    en caso contario al terminar el ciclo y ser distinto de 0 quiere decir que no hay la misma cantidad de pares y se da como falso el restutado
    se van a tomar los valores H[0] para caracteres aleatorios y H[1] para par de parentesis
    siendo key= a para par de parentesis y key=b para caracteres aleatorios
    """
    for element in string:
        if element =="(" or element==")":
            count= dictSearch(hash_table,"a")
            if count and count >= 0:
                if element=="(":
                    dictUpdate(hash_table,"a",count +1)
                else:
                    dictUpdate(hash_table,"a",count -1)
            else:
                if not count:
                #inserta el primer elemento en caso de ser "("
                    if element=="(":
                        dictInsert(hash_table,"a",1)
                    else: 
                        return False
                else:
                    return False                
        else:    
            count= dictSearch(hash_table,"b")
            if count:
                dictUpdate(hash_table,"b",count+1)
            else:
                dictInsert(hash_table,"b",1)
    
    print("PRINT HASHTABLE")
    print("[",end="")
    for element in hash_table:
        if element:
            print("(",element.head.value.key,":",element.head.value.value,end="),")
        else:
            print("( NONE )",end=",")
    print("]")
    
    if hash_table[1].head.value.value==0:
        return True
    else:
        return False
        #==========================#
                #Ejercicio7
        #==========================#
def reduceLen(string):

    count=0
    prev_element=""
    new_string=""
    for element in string:
        if prev_element=="":
            prev_element=element
            count += 1
        else:
            if element==prev_element:
                count += 1
            else:
                if count % 2 !=0:
                    new_string += prev_element

                prev_element= element
                count=1
    if count % 2!= 0:
        new_string += prev_element

    return new_string
        #==========================#
                #Ejercicio8
        #==========================#
def isContained(string,string_patron):
    estado= len(string_patron)

    count_estados=0
    for element in string:
        if element== string_patron[count_estados]:
            count_estados+= 1
        
        if count_estados == ( len(string_patron) ):
            return True

        if count_estados+1 < len(string_patron):
            if element== string_patron[count_estados + 1]:
                return False

    return False
#======================================================#

if __name__ == '__main__':

    """
    
    print("is Palindrome de \"anitalavalatina\"",isPalindrome("anitalavalatina"))
            
    print("el caracter mas repetido en \"aaabcddba\": ",mostRepeatedChar("aaabcddba"))

    print("la isla mas grande en \"cdaaaaaasssbbb\": ",getBiggestIslandLen("cdaaaaaasssbbb"))

    """

    hola= "(ccc(ccc)cc((ccc(c))))"

    print("la cadena \"",hola,"\" tiene sus parentesis balanceados : ", verifyBalancedParentheses( hola ))

    hola= ")ccc(ccc)cc((ccc(c)))("

    print("la cadena \"",hola,"\" tiene sus parentesis balanceados : ", verifyBalancedParentheses( hola ))

    print("la cadena \"  aaabccdabbddd \" se va a reducir a: ",reduceLen("aaabccdabbddd"))