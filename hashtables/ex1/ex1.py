#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length * 2)

    """
    YOUR CODE HERE
    """
    for x in range(len(weights)):
        hash_table_insert(ht, weights[x], x)
    answer = None
    for x in range(len(weights)):
        target = limit - weights[x]
        current = weights[x]
        current_index = x
        valid = hash_table_retrieve(ht, target)
        if valid is not None:
            if x > valid: answer = (x, valid)
            else: answer = (valid, x)
            return answer
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
