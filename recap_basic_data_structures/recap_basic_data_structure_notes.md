# Recap Basic Data Structures 

## Data Structures with descriptions 

1. **Record (struct)**: A data structure that stores subitems (also called *fields*) with names associated with each subitem.
    
    ### Record
    - **General Concept**: A record is a general term used to describe a collection of related data items, often used in databases and data structures.
    - **Implementation**: In C++, records are typically implemented using `struct` or `class`.

    #### Key Differences
    - **Default Access Control**: `struct` members are public by default, while `class` members are private by default.
    - **Use Cases**: `struct` is typically used for plain data structures, while `class` is used for objects that require encapsulation (data and methods are in the class for security) and additional functionality.
    - **Flexibility**: Both `struct` and `class` can have member functions, constructors, destructors, and access specifiers (public, private, protected).

   
2. **Array**: A data structure that stores an ordered list of items, where each item is accessible by its index.

3. **Linked List**: A data structure that stores an ordered list of items in *nodes*, where each node stores data and has a pointer to the next node.

4. **Binary Tree**: A tree-like data structure where each node stores data and can have up to two children (often called the *left child* and *right child*).

5. **Hash Table**: A data structure that stores unordered items by mapping (or *hashing*) each item to a specific location in an array.

6. **Heap**:
   - **Max-Heap**: A tree where each node's key is greater than or equal to the keys of its children.
   - **Min-Heap**: A tree where each node's key is less than or equal to the keys of its children.

7. **Graph**: A data structure representing connections among items. It consists of *vertices* (items) connected by *edges*. An *edge* represents a connection between two vertices in a graph.

Choosing the right data structure depends on the use. For example, if a program requires fast insertion of new data, a linked list my be a better choice than an array 

---

## Abstract Data Type (ADT)

An *Abstract Data Type (ADT)* is a data type defined by a set of operations that can be performed on it, without specifying how these operations are implemented. ADTs can be built using different underlying data structures, but the user doesn’t need to know the details of the implementation to use the ADT effectively. 

For example, a *list* is a common ADT. We use functions like `append` and `remove` to manipulate the list without needing to understand how these operations are executed internally. 

---

Here’s a refined version:

---

## Common Abstract Data Types (ADTs)

1. **List**: Holds an ordered collection of data. Common underlying data structures: Array, Linked List.

2. **Dynamic Array**: Holds ordered data with indexed access, allowing for dynamic resizing. Common underlying data structure: Array.

    - **Dynamic Array**: This is a general term for an array that can resize itself when elements are added or removed. It provides random access to elements and typically doubles its size when it runs out of space.
    - **Vector**: In C++, a vector is a specific implementation of a dynamic array provided by the Standard Template Library (STL). It offers additional functionalities like automatic resizing, iterators, and member functions for easier manipulation.

3. **Stack**: Allows insertion and removal of items only at the top of the stack (LIFO - Last In, First Out). Common underlying data structure: Linked List.

4. **Queue**: Allows insertion of items at the end and removal from the front (FIFO - First In, First Out). Common underlying data structure: Linked List.

5. **Deque** (pronounced "deck," short for *double-ended queue*): Allows insertion and removal of items at both the front and back. Common underlying data structure: Linked List.

6. **Bag**: Stores items where the order does not matter, and duplicates are allowed. Common underlying data structures: Array, Linked List.

7. **Set**: Stores a collection of distinct items, where duplicates are not allowed. Common underlying data structures: Binary Search Tree, Hash Table.

8. **Priority Queue**: Each item has a priority, and items with higher priority are closer to the front of the queue. Common underlying data structure: Heap.

9. **Dictionary (Map)**: Associates or maps keys to values, allowing efficient lookup by key. Common underlying data structures: Hash Table, Binary Search Tree.

---

## Application of ADT's 

### Abstraction, optimization & ADT's in Standar Libraries 

- Using abstract data types allows programmers to focus on higher level operations, howeber underlying implementation is needed to analyze or improve runtime efficiency 

#### Standard Libraries 

- Most programming languages provide a standard library that implements common abstract data types (ADTs).
- Some languages allow programmers to choose the underlying data structure used for the ADTs.
- Other programming languages may use a specific data structure to implement each ADT or may automatically choose the underlying data structure.


| Programming Language | Library                          | Common Supported ADTs                      |
|----------------------|----------------------------------|--------------------------------------------|
| Python               | Python standard library          | list, set, dict, deque                     |
| C++                  | Standard Template Library (STL)  | vector, list, deque, queue, stack, set, map|
| Java                 | Java collections framework (JCF) | Collection, set, list, map, queue, deque   |


Does this work for you?
