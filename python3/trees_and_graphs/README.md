# Trees and Graph

## Easy

+ [binary_tree_paths.py](binary_tree_paths.py)
  - Find all root-to-leaf paths in a binary tree.

+ [Diameter of Binary](diameter_of_binary_tree.py)
  - Compute the diameter (or width) of a binary tree. 

+ [flood_fill.py](flood_fill.py):
  - Flood fill a 2-D image.

+ [Invert Tree](invert_tree.ipynb)
  - Invert a binary tree.

+ [Symmetric Tree](symmetric_tree.ipynb)
  - Given a binary tree, check whether it is a mirror of itself
    (ie, symmetric around its center).
  - See Also: [level_order_traversal.py](level_order_traversal.py)


## Medium

+ [Account Merge.py](account_merge.ipynb) *
  - Merge duplicates account records with name and a list of emails.
  - A good practice on dictionary and set.

+ [bipartite_graph.py](bipartite_graph.py)
  - Given an undirected graph, return true if and only if it is bipartite.
 
+ [bst_to_double_linked_list.py](bst_to_double_linked_list.py) *
  -  Convert a Binary Search Tree (BST) to a sorted Circular Doubly-Linked List in place.

+ [clone_undirected_graph.py](clone_undirected_graph.py)
  - Deep copy a graph.

+ [Course Schedule](course_schedule.ipynb) *
  - Given the total number of courses and a list of prerequisite pairs, is it
    possible for you to finish all courses?
  - Category: topological sorting.
  - See Also: [alien_dictionary](alien_dictionary.ipynb),  [topological sort](topological_sort.ipynb)
 
+ [Decode String](decode_string.py)
  - Decode k[s] as k * s, where k is a positive number and s may contain other encodings.\
  - Techniques: recurssion and stack.
 
+ [flatten_binary_tree_to_linked_list.py](flatten_binary_tree_to_linked_list.py)
  - Given a binary tree, flatten it to a linked list in-place.

+ [level_order_traversal.py](level_order_traversal.py)
  - Given a binary tree, return the level order traversal of its nodes' values. 
    (ie, from left to right, level by level).
  - See Also: [zipzag_level_traversal.py](zipzag_level_traversal.py)

+ [lowest_common_ancestor_binary_tree.py](lowest_common_ancestor_binary_tree.py) [M]
  - Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
  - Try to traverse the tree only once.

+ [number_of_islands.py](number_of_islands.py)
  - Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
   
+ [Right-side View of Tree](right_side_view_of_tree.py)
  - Given a binary tree, imagine yourself standing on the right side
    of it, return the values of the nodes you can see ordered from top to bottom.

+ [Topological Sort](topological_sort.ipynb) *
   - Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.
  - Given a directed graph, find the topological ordering of its vertices.
  - Category: topological sorting.
  - See Also:  [Course Schedule I](course_schedule.py)
 
+ [Validate Binary Search Tree.py](validate_binary_search_tree.py) [M]
  - Determine if binary tree is a valid Binary Search Tree (BST).
 
+ [Vertical Traversal](vertical_traversal.py)
  - Get the binary tree values in the 'vertical' order, from left to right.

+ [Zipzag Level Traversal](zipzag_level_traversal.py)
  - Given a binary tree, return the zigzag level order traversal of its nodes' values. 
    (ie, from left to right, then right to left for the next level and alternate between).
  - See Also: [level_order_traversal.py](level_order_traversal.py)


## Hard

+ [Alien Dictionary](alien_dictionary.ipynb) *
  - Given a sorted dictionary of an alien language, find order of characters in the language.
  - Category: topological sorting.
  - See Also: [course_schedule.py](course_schedule.py) and [Topological Sort](topological_sort.py)

+ [Cut off Trees](cut_off_trees.py)
  - Given a forest (2D array) of trees of different heights, find the number of steps
    to cut them according to their height order.  
  - Note: Not a "green" problem. 

* [Max Path Sum in a Binary Tree](max_path_sum.ipynb) *
  - Find the maximum path sum in a binary tree.
  - Category: DFS
  - See Also: [Odd Network](odd_network.ipynb)

* [Odd Network](odd_network.ipynb) *
  - Number of odd-link connections in network (tree).  
  - See Also: [Max Path Sum in a Binary Tree](max_path_sum.ipynb)
  
* [Shortest Distance from all Buildings](shortest_distance_from_all_buildings.ipynb)
  - Find the shortest total distance to all buildings in a grid.
  - Category: DFS
  - Category: BFS
   
* [Word Ladder](word_ladder.ipynb) *
  - Given two words (beginWord and endWord), and a dictionary's word list, find the
    length of shortest transformation sequence from beginWord to endWord, such that
    only one letter can be changed at a time.  Return length of the ladder.
  - Categories: Pattern Index, BFS, Bi-BFS.


##  Utilities

+ [shared_utils.py](shared_utils.py)
  - class: TreeNode
  - functions: make_tree, tree_to_list, ...

  