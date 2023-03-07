
import numpy as np
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
#Paraméterei: mérete (tupel-ként), default mérete pedig legyen egy (2,2)
#Be: (2,2)
#Ki: [[0,0],[0,0]]
#create_array()

def create_array(merete = (2,2)):
    return np.zeros(merete)

#print(create_array())    

#Készíts egy függvényt ami a paraméterként kapott array-t főátlót feltölti egyesekkel
#Be: [[1,2],
#     [3,4]]
#Ki: [[1,2],
#     [3,1]]
#set_one()

def set_one(array):
    np.fill_diagonal(array, 1)
    return array

#print(set_one(np.array([[1,2],[3,4]])))

# Transzponáld a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()
def do_transpose(array):
    return np.transpose(array)

#print(do_transpose([[1, 2], [3, 4]]))

# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, alapértelmezetten 
# Be: [0.1223, 0.1675], n = 2
# Ki: [0.12, 0.17]
# round_array()

def round_array(array, n=2):
    return np.round(array, n)

#print(round_array([0.1223, 0.1675], 2))

# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 0 - False-ra az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()

def bool_array(array):
    return np.bitwise_not(np.logical_not(array))

#print(bool_array(np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]])))

# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()

def invert_bool_array(array):
    return np.logical_not(array)

#print(invert_bool_array(np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]])))

# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()

def flatten(array):
    return array.flatten()

#print(flatten(np.array([[1,2], [3,4]])))