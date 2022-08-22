array_A = input()
array_B = input()
# print(list(array_A))

def Suffix_Automaton(array1 , array2):
    #check for suffix automation
    Automaton = False
    array1 = list(array1)
    array2 = list(array2)
    word_list =[]
    index_tracker = 0
    for i in range(len(array2)):
        for j in range(i, len(array1)):
            if array2[i] == array1[j] and j >= index_tracker:
                index_tracker = j
                word_list.append(array1[j])
                break
    if word_list == array2:
        Automaton = True
    return Automaton

def Suffix_Array(sarray1 , sarray2):
    Suffix_Array = False
    if len(sarray1) != len(sarray2):
        return Suffix_Array
    if sorted(list(sarray1)) == sorted(list(sarray2)):
        Suffix_Array = True
    # print(sorted(list(sarray1)))
    # print(sorted(list(sarray2)))
    return Suffix_Array


def need_tree(na1, na2):
    need_tree = False
    list1 = list(na1).copy()
    list2 = list(na2).copy()
    for elm in list2:
        if elm in list1:
            list1.remove(elm)
        else:
            need_tree = True
            return need_tree
    # print(list1)
    return need_tree


def Suffix_Structures(A1, A2):
    if need_tree(A1, A2) == True:
        return print('need tree')
    if Suffix_Array(A1, A2)== True:
        return print('array')
    elif Suffix_Automaton(A1, A2) == True:
        return print('automaton')
    return print('both')



# print(Suffix_Array(array_A, array_B))
#
# print(Suffix_Automation(array_A, array_B))
Suffix_Structures(array_A, array_B)