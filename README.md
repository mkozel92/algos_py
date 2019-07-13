# algos_py

Implementation of common algorithms and data structures in python

#### Contents
* [Binary tree algos](#binary-tree-algos)
  * _binary_tree_
  * _bst_sequences_
  * _common_ancestor_
  * _connect_same_level_
  * _count_from_range_
  * _elements_from_range_
  * _is_balanced_
  * _is_bst_
  * _min_tree_
* [Bit manipulation](#bit-manipulation)
  * _convert_
  * _float_to_bin_
  * _insert_
  * _longest_sequence_
* [Compression](#compression)
  * _run_length_compression_
  * _huffman_compression_
* [Data structures](#data-structures)
  * _binary_heap_
  * _bst_symbol_table_
  * _chained_hash_table_
  * _linear_probed_hash_table_
  * _linked_list_queue_
  * _linked_list_stack_
  * _r_way_trie_
  * _red_black_tree_
  * _resizing_array_stack_
  * _ternary_search_trie_
* [Dynamic connectivity](#dynamic-connectivity)
  * _quick_find_
  * _quick_union_
  * _weighted_quick_union_
* [Dynamic programming](#dynamic-programming)
  * _coins_
  * _longest_common_subsequence_
  * _max_independent_set_
  * _triple_step_
* [Graphs](#graphs)
  * [Shortest path](#shortest_path)
    * _Bellmann_Ford_
    * _Dijkstra_

#### Binary tree algos

1. _binary_tree_  
  simple implementation of binary tree. \
O(log N) insertion and O(log N search)

1. _bst_sequences_  
  Return all possible sequences that could have been used to construct given binary tree
  Complexity O(N!)

1. _common_ancestor_  
  Find earliest common ancestor in binary tree\
  complexity O(N)

1. _connect_same_level_  
  Algo to connect tree nodes that are on the same level in the tree. \
Uses DFS and has O(N) complexity

1. _count_from_range_  
function to count elements of tree that are lower than given element, higher then given element \
of fall in given rage. All are recursive algos with O(log N) complexity.
This algos assume that each node keep size of its subtree

1. _elements_from_range_  
  enqueues elements that fall in specified range with O(M + log N) complexity

1. _is_balanced_  
  checks if given tree is balances (no to subtrees have height difference bigger than 1)\
  complexity O(N)
  
1. _is_bst_  
  check if given tree is bst\
  complexity O(N)

1. _min_tree_  
  build a tree of minimal height given a list of keys \
  complexity O(N log N) 

#### bit manipulation

1. _convert_  
  count how many bits need to be flipped to convert given integer into another integer
  
1. _float_to_bin_  
  convert decimal part of given float into bit representation
  
1. _insert_  
  insert bits of given int into another into between specified bits

1. _longest_sequence_  
  return length of the longest sequence of 1 bits in given integer\
  that can be created by flipping one bit

#### compression

1. _run_length_compression_  
  compress data by encoding alternating sequences of same bits as a lengths of those sequences


1. _huffman_compression_  
  compress data using huffman encoding

#### data structures

1. _binary_heap_  
  implementation of binary heap using an array of fixed size. \
  O(log N) insertion, deletion and search

1. _bst_symbol_table_  
  symbol table (holds key, value pairs) implemented using binary tree. \
  O(N) deletion, search and insertion as balance is not ensured. \
  O(log N) deletion, search and insertion if the tree is balanced \
  but Hibbard deletion is not symmetric and messes up the balance

1. _chained_hash_table_  
  hash table implementation using separate chaining. \
  O(N/M) insertion, deletion and search. \
  N/M is num_of_elements/size_of_array = average_list length

1. _linear_probed_hash_table_  
  hash table implemented using linear probing. \
  O(N) insert and search but basically O(1) if the table is max half full

1. _linked_list_queue_  
  simple implementation of a queue using a linked list. \
  O(1) enqueue, dequeue and peek

1. _linked_list_stack_  
  simple implementation of a stack using a linked list. \
  O(1) push, pop, peek

1. _r_way_trie_  
  implementation of a trie
  O(k) put and get where k is length of key
    

1. _red_black_tree_  
  red black binary tree. Inserting of new elements keeps the tree balanced. \
  O(log N) search, insert 

1. _resizing_array_stack_  
  stack implemented using resizing array \
  amortized constant push and pop. \
  O(N) for if the pop or push resize underlying array

1. _ternary_search_trie_  
  implementation of ternary trie. \
  it has same performance as r_way trie but is more memory efficient \
  because it does not hold tons of empty links
  
#### dynamic connectivity

keeps track of connected components \
Union(p, q) - connects two elements \
connected(p, q) - checks if elements are connected \


1. _quick_find_  
  O(N) union\
  O(1) connected

1. _quick_union_  
  O(N) union\
  O(N) connected

1. _weighted_quick_union_
  O(log N) union\
  O(log N) connected\
  But those are basically constant because average case complexity \
  grows proportionally to inverse Ackermann function = does not grow at all 
    
#### dynamic programming

1. _coins_  
  count all the different ways to get given change using given coins
  complexity O(MN) ..num_coins * change to get
  
1. _longest_common_subsequence_  
  return length of longest common subsequence \
  complexity O(MN)
  
1. _max_independent_set_  
  get sum of elements of max independent set. \
  Independent set is subset of a list such that no elements in this set \
  where consecutive in the original list
  complexity O(N)
  
1. _triple_step_  
  count ways to go up the stair using 1,2, or 3 steps at time
  complexity O(MN)...choices of steps * num of steps to climb
    
    

#### graphs

##### shortest path

1. _Bellman_Ford_  
  Bellman Ford shortest path algo. \
  relaxes every edge V times. \
  Works with cyclic graphs with negative edges and can detect negative cycles. \
  complexity O(EV)

1. _Dijkstra_  
  Dijkstra shortest path algo. \
  works for cyclic graphs with no negative edges. \
  complexity O(E log V)
  

##### 1. adjacency_list_graph

graph represented by adjacency list. \
O(1) add_edge \
O(1) return adjacent vertices for given vertex\
space complexity E + V

##### 2. adjacency_matrix_graph

graph represented by adjacency matrix. \
O(1) add_edge \
O(N) return adjacent vertices for given vertex\
space complexity V^2

##### 3. breadth_first_search

just BFS, O(E + V)

##### 4. depth_first_search

just DFS, O(E + V)

##### 5. connected_components

check if there is a path between two vertices in O(1) time. \
O(E + V) to build CC object using DFS

#### recursion

##### 1, permutations

get every permutation of given string in O(N!)

##### 2. squashable_words

Checks if a word can be recursively reduced to an empty string in such a way\
that after removing a letter from current word the new word is still in a \
dictionary of valid words \
O(N!)


#### search

##### 1. binary_search

both recursive and iterative implementations of binary search\
O(log N)

##### 2. kth_largest

find kth largest element in a given list\
implemented using quick sort partitioning\
O(N) but random shuffling ensures O(N log N) and in practise runs in linear time

#### sort

##### 1. heap_sort

inplace, unstable, O(N log N)

##### 2. insertion_sort

inplace, stable, O(N^2)

##### 3. knuth_shuffle

ensures uniformly random inplace shuffle in O(N)

##### 4. merge_sort

both recursive and iterative implementations\
not-inplace, stable, O(N log N)

##### 5. quick_sort

inplace, unstable\
O(N^2) but random shuffling ensures O(N log N) \

three way partitioning ensures O(N log N) even for duplicate keys

##### 5. selection_sort

inplace, unstable, O(N^2)

##### 6. shell_sort

inplace, unstable, O(nobody really knows)
