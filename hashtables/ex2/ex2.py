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
    for x in range(len(tickets)):
        hash_table_insert(hashtable, tickets[x].source, tickets[x].destination)
    source = "NONE"
    for x in range(len(route)):
        dest = hash_table_retrieve(hashtable, source)
        route[x] = dest
        source = dest
    return route
