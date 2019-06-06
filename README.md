# algos_py

Implementation of common algorithms and data structures in python


####Binary tree algos

#####1. binary_tree

simple implementation of binary tree. \
O(log N) insertion and O(log N rearch)

#####2. connect_same_level

Algo to connect tree nodes that are on the same level in the tree. \
Uses DFS and has O(N) complexity

#####3. count_from_range

function to count elements of tree that are lower than given element, higher then given elemtnt \
of fall in given rage. All are recursive algos with O(log N) complexity.
This algos assume that each node keep size of its subtree

#####4. elements_from_range

enqueues elemnts that fall in specified range with O(M + log N) complexity

####data structures

#####1. binary_heap

implementation of binary heap using an array of fixed size. \
O(log N) insertion, deletion and search

#####2. bst_symbol_table

symbol table (holds key, value pairs) implemented using binary tree. \
O(N) deletion, search and insertion as balance is not ensured. \
O(log N) deletion, search and insertion if the tree is balanced \
but Hibbard deletion is not symmetric and messes up the balance

#####3. chained_hash_table

hash table implementation using separate chaining. \
O(N/M) insertion, deletion and search. \
N/M is num_of_elements/size_of_array = average_list length

#####4. linear_probed_hash_table

hash table implemented using linear probing. \
O(N) insert and search but basically O(1) if the table is max half full

#####5. linked_list_queue

simple implementation of a queue using a linked list. \
O(1) enqueue, dequeue and peek

#####6. linked_list_stack

simple implementation of a stack using a linked list. \
O(1) push, pop, peek

#####7. red_black_tree

red black binary tree. Inserting of new elements keeps the tree balanced. \
O (log N) search, insert 

#####8. resizing_array_stack

stack implemented using resizing array \
amortized constant push and pop. \
O(N) for if the pop or push resize underlying array

####dynamic connectivity

keeps track of connected components \
Union(p, q) - connects two elements \
connected(p, q) - checks if elements are connected \


#####1. quick_find
O(N) union\
O(1) connected

#####2. quick_union
O(N) union\
O(N) connected

#####2. weighted_quick_union
O(log N) union\
O(log N) connected

####graphs

#####1. adjacency_list_graph

graph represented by adjacency list. \
O(1) add_edge \
O(1) return adjacent vertices for given vertex\
space complexity E + V

#####2. adjacency_matrix_graph

graph represented by adjacency matrix. \
O(1) add_edge \
O(N) return adjacent vertices for given vertex\
space complexity V^2

#####3. breadth_first_search

just BFS, O(E + V)

#####4. depth_first_search

just DFS, O(E + V)

#####5. connected_components

check if there is a path between two vertices in O(1) time. \
O(E + V) to build CC object using DFS

####recursion

#####1, permutations

get every permutation of given string in O(N!)

#####2. squashable_words

Checks if a word can be recursively reduced to an empty string in such a way\
that after removing a letter from current word the new word is still in a \
dictionary of valid words \
O(N!)


####search

#####1. binary_search

both recursive and iterative implementations of binary search\
O(log N)

#####2. kth_largest

find kth largest element in a given list\
implemented using quick sort partitioning\
O(N) but random shuffling ensures O(N log N) and in practise runs in linear time

####sort

#####1. heap_sort

inplace, unstable, O(N log N)

#####2. insertion_sort

inplace, stable, O(N^2)

#####3. knuth_shuffle

ensures uniformly random inplace shuffle in O(N)

#####4. merge_sort

both recursive and iterative implementations\
not-inplace, stable, O(N log N)

#####5. quick_sort

inplace, unstable\
O(N^2) but random shuffling ensures O(N log N) \

three way partitioning ensures O(N log N) even for duplicate keys

#####5. selection_sort

inplace, unstable, O(N^2)

#####6. shell_sort

inplace, unstable, O(nobody really knows)









