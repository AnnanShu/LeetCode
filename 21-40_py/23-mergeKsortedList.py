# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        # list_idx = [i for i in range(len(lists))]
        len()
        
            





import numpy as np 
def k_way_merge(*lists:list):
    '''
    We assume that all list here have the same length and the length are greater than or equal to 1.
    '''
    # initialize merged list
    merged_list = list()
    #get k and n value
    k = len(lists)
    n = len(lists[0])
    # Initialize pointers of all lists 
    indices = np.array([0] * k)
    while any(indices < n):
        # get each first element of those k lists, If the list already at the end, add an infinite number to keep the position
        top_list = [lists[i][indices[i]] if indices[i] < n else np.Inf for i in range(k)]
        min_index = top_list.index(min(top_list))
        # Add the 
        merged_list.append(top_list[min_index])
        # Move the index in which list with the smallest value 1 step.
        indices[min_index] += 1

    return merged_list 