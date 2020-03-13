#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #using the source as a key to find destinations

    #this first for loop inserts all tickets into hashTable
    sources = []
    for place in tickets:
        source = place.source
        sources.append(source)
        destination = place.destination
        # print(source, ' and ', destination)
        hash_table_insert(hashtable, source, destination)

    trip = []
    # print(sources, 'SDFHJGYDHTDGF')

    #use None as key to find the first destination
    ret = hash_table_retrieve(hashtable, 'NONE')
    while ret is not 'NONE':
        trip.append(ret)
        ret = hash_table_retrieve(hashtable, ret)

    print('FINAL TRIP', trip)
    return trip

