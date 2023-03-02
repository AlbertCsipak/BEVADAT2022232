# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
evenList = [2,4,6,8]
oddList = [1,3,5,7]
mixedList = [1,2,3,4,5,6,7,8,9]

# %%
def contains_odd(input_list):
    for i in input_list:
        if i % 2 == 1:
            return True
    return False

# %%
print(contains_odd(oddList))
print(contains_odd(evenList))
print(contains_odd(mixedList))

# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list):
    tmpList = []

    for i in input_list:
        if i % 2== 0:
            tmpList.append(False)
        else:
            tmpList.append(True)
    return tmpList

# %%
print(is_odd(oddList))
print(is_odd(evenList))
print(is_odd(mixedList))

# %%

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list_1, input_list_2):
    tmpList = []
    for i in range(0,len(input_list_1),1):
        tmpList.append(input_list_1[i] + input_list_2[i])
    return tmpList

# %%
print(element_wise_sum(evenList, oddList))

# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'address': '123 Main Street',
    'city': 'New York',
    'country': 'USA'
}

# %%
def dict_to_list(input_dict):
    outputList = []
    for key, value in input_dict.items():
        tmp=key,value
        outputList.append(tmp)
    return outputList

# %%
print(dict_to_list(person))

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


