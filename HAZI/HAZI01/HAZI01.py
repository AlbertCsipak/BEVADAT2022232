# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list,start_index,end_index):
    return input_list[start_index:end_index]

# %%
#print(subset([1,2,3,4,5,6,7,8,9],3,6))
#print(subset([],3,6))

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list,step_size):
    tmpList = []
    for i in range(0,len(input_list),step_size):
        tmpList.append(input_list[i])
    return tmpList

# %%
#print(every_nth([1,2,3,4,5,6,7,8,9],2))
#print(every_nth([],10))

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    isUnique = False
    for i in input_list:
        if input_list.count(i) < 2:
            isUnique = True
        else:
            isUnique = False
    return isUnique

# %%
#print(unique([1,1,1]))
#print(unique([1,1,2]))
#print(unique([]))


# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    tmpList = []

    for item in input_list:
        for value in item:
            tmpList.append(value)
    return tmpList

# %%
#print(flatten([[1,2,3,4],[5,6,7,8]]))
#print(flatten([[]]))

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    tmpList = []
    for arg in args:
        tmpList+=arg
    return tmpList

# %%
#print(merge_lists([1,2,3,4], [5,6,7,8]))
#print(merge_lists([],[]))

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    tmpList = []
    for i in input_list:
        tmpList.append((i[1], i[0]))
    return tmpList

# %%
#print([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)])
#print(reverse_tuples([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]))

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_duplicates(input_list):
    tmpList = []
    for i in input_list:
        if i not in tmpList:
            tmpList.append(i)
    return tmpList

# %%
#print(remove_duplicates([1,1,1,2,2,2,3,3,3,4,4,4]))
#print(remove_duplicates([0]))

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    transposed = []
    if len(input_list) > 1:
        for i in range(len(input_list[1])):
            tmpList = []
            for j in range(len(input_list[0])):
                tmpList.append(input_list[j][i])
            transposed.append(tmpList)    
    return transposed

# %%
#print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
#print(transpose([[]]))

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list,chunk_size):
    retList = []
    tmp = []
    counter = 0

    for i in input_list:
        for j in i:
            tmp.append(j)
            counter += 1
            if counter == chunk_size:
                retList.append(tmp)
                counter = 0
                tmp = []

    retList.append(tmp)

    return retList

# %%
#print(split_into_chunks([[1,2,3],[4,5,6],[7,8,9]], 2))

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    merged_dict={}
    for item in dict:
        merged_dict=merged_dict | item
    return merged_dict

# %%
#person1 = {
#    "name": "John",
#    "age": 20
#}
#person2 = {
#    "address": "123 Main Street",  
#}
#print(merge_dicts(person1, person2))


# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    parityDict = {
        'even':[],
        'odd':[]
    }

    for i in input_list:
        if i%2==0:
            parityDict['even']+=[i]
        else:
            parityDict['odd']+=[i]

    return parityDict

# %%
#print(by_parity([1,2,3,4,5,6]))

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    for key in input_dict.keys():
        sum = 0
        count = 0
        for value in input_dict[key]:
            sum += value
            count += 1
        input_dict[key] = sum/count

    return input_dict

# %%
#mean_key_value({
#    "even" : [2,4,6,8],
#    "odd" : [1,3,5,7]
#})

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


