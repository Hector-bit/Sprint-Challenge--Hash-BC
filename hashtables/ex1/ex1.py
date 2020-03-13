#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # if length == 1:
    #     return None 
    # #will loop in range of length to give indices 
    # for i in range(length): 
    #     print('INDICES', i)
    #     #difference will be the key we will search for
    #     drff = limit - weights[i]
    #     #inserting key = weight and value is the index
    #     hash_table_insert(ht, weights[i], i)
    #     #retrieving with key = weight
    #     retrieved = hash_table_retrieve(ht, diff)
    #     print(retrieved, 'RETRIEVED VALUE')
    #     total = weights[i] + weights[retrieved]
    #     print('checking types', type(limit), type(total))
    #     if total == limit:
    #         return (retrieved, weights[i])
    # print(ht.storage)
    # print(index, 'this is index') 
    # return index

    #loops through wieghts and puts them in the hashTable
    for index in range(length):
        hash_table_insert(ht, weights[index], index)

    for weight in weights:
        #for loop through each element in weights to get first index
        index_one = hash_table_retrieve(ht, weight)
        #diff will be the key we use to find the second index
        diff = limit - weights[index_one]
        index_two = hash_table_retrieve(ht, diff)
        if index_one != None and index_two != None:
            if weights[index_one] < weights[index_two]:
                print(f'{weights[index_one]} + {weights[index_two]} = {limit}, {index_one}, {index_two}')
                return (index_two, index_one)
            else:
                print(f'{weights[index_one]} + {weights[index_two]} = {limit}, {index_one}, {index_two}')
                return (index_two, index_one)
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


