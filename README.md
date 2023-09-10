# Data Structures in Python

### What they do:

**LinkedListsBasic:**<br/>
It defines a simple linked list data structure and various methods to manipulate it, such as deleting or inserting nodes, and printing the list.<br />

**BinarySearch:**<br/>
It defines two implementations of binary search algorithms used to search for a target element in a sorted list. The first is recursive, and the other is iterative.

**BinaryTrees:**<br/>
It implements a binary search tree data structure along with various functions to manipulate and traverse the tree.

**sort:**<br/>
It contains implementations of various sorting algorithms, like selection sort, bubble sort, insertion sort, and heap sort.

### How I built them:

For each of them I created some helping functions:
- For LinkedListsBasic, Node class represents individual nodes in the linked list. Each node has two attributes: val, which stores the value of the node, and next, which points to the next node in the list. By default, val is set to Node and next is set to None.
- The LinkedList class represents a linked list and has an attribute head, which is initially set to None.
- The insert method inserts a new node with the given value val at the end of the linked list; it first creates a new Node with the provided value; if the linked list is empty, it sets the new node as the head of the list; otherwise, it traverses the list to find the last node and appends the new node to the end.
- printLL prints the values of all nodes in the linked list by traversing it from the head to the end.
- insertMid inserts a new node with the given value val after a node with a value of 3 in this case; it traverses the linked list and looks for a node with a value of 3; when it finds such a node, it inserts the new node with the given value after it.
- deleteLast deletes the last node in the linked list; it traverses the list until it reaches the second-to-last node and then sets its next attribute to None.
- delete deletes the first occurence of a node with the specified value val from the linked list; it traverses the list and looks for the node with the specified value; when it finds such a node, it adjusts the next pointers to skip the node to remove it from the list.
- deleteFirst deletes the first node in the linked list by updating the head to point to the second node in the list.
<!-- -->
- For BinartSearch, the parameters are: l, the sorted list to search in, x, the target element to search for, low, the index representing the lower bound of the search range, and high, the upper bound.
- search1 represents the recursive approach; the function first checks if low is less than or equal to high; if not, the target element x is not in the list, so it returns -1; if low is less than or equal to high, it calculates the mid index as the average of low and high; it then compares the element and index mid with the target element x; if they are equal, the function returns the index mid, indicating that x was found at this position in the list; if the element at index mid is greater than x, it recursively calls search1 on the left half of the list (from low to mid-1); if the element at index mid is less than x, it recursively calls search1 on the right half of the list (from mid+1 to high); this process continues until the target element x is found or until the search range is exhausted.
- search2 represents the itterative approach; it uses a while loop to repeatedly search for a target element; inside the loop, it calculates the mid index as the average of low and high; it then computes the element at index mid with the target element x; if they are equal, the function returns the index mid, indicating that x was found at this position in the list; if the element at index mid is less than x, it updates the low index to mid+1, effectively reducing the search range to the right half of the list; if the element at index mid is greater than x, it updates the high index to mid-1, effectively reducing the search range to the left half of the list; this process continues until the target element x is found or until low becomes greater than high, indicating that x is not in the list.
<!-- -->
- For BinaryTrees, the Node class represents a node in the BST. Each node has three attributes: left, points to the left child node, right, points to the right child node, and val, which stores the value of the node.
- insert inserts a new node with the given value val; if the root is None, it creates a new node with the given value and returns it as the new root; if the root node is not None, it traverses the tree to find the right position to insert the new node; it does this by comparing the val with the values of nodes and recursively calling insert on either the left subtree or the right one; the function returns the modified root.
- get_min returns the minimum value in the BST; it starts at the root and then traverses the left child nodes until it reaches the leftmost node, which contains the minimum value.
- get_max is similar with the previous one.
- inorder performs an inorder traversal of the BST; the nodes are visited in ascending order, which means that the left subtree is explored first, followed by the current node, and then the right subtree; it prints the values of nodes in ascending order.
- preorder performs a preorder traversal of the BST; the current node is visited before its children; the order is root-left-right; it then prints the values of nodes in preorder.
- In postorder, the children of the current node are visited before the node itself; the order is left-right-root.
<!-- -->
- sort has implementations of various sorting algorithms.
- selectionSort works by repeatedly finding the minimum element from the usorted part of the list and moving it to the beginning; it iterates through the list and maintains a min_index variable to keep track of the index of the minimum element in the remaining unsorted part of the list; it swaps the element at the current index with the element at the min_index after each iteration.
- bubbleSort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order; it continues this process until no swaps are required, indicating that the list is sorted.
- insertionSort builds the final sorted list one item at a time; it starts with the second element in the list and compares it to the elements in the already sorted part of the list; it inserts the elements in its correct position within the sorted part of the list by shifting other elements to the right.
- heapify takes a List, its length n, and an index i; it compares the element at index i with its left and right children (if they exist) and swaps the element with the largest child necessary; this function ensures that the max-heap property is maintained.
- heapSort first builds a max heap from the elements in the list by repeatedly calling heapify; after building the max heap, it repeatedly extracts the maximum element (at the root) and places it at the end of the list.

### Challenges I ran into:

