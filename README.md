# Linked Lists and Recursion Lab

## Overview

This project demonstrates how linked lists and recursion work together in Python.

The program includes:

* A `Node` class to store data and references
* A `LinkedList` class for managing nodes
* Recursive methods for:

  * Summing node values
  * Searching for a value
  * Reversing the linked list

This lab focuses on understanding recursive traversal and manipulation of node-based data structures.

---

## Features

### Insert at Front

Adds a node to the beginning of the linked list.

### Insert at End

Adds a node to the end of the linked list.

### Recursive Sum

Uses recursion to calculate the total of all node values.

### Recursive Search

Uses recursion to determine whether a target value exists in the list.

### Recursive Reverse

Uses recursion to reverse the linked list in-place.

---

## Project Structure

```bash
.
├── linked_list.py
├── test_linked_list.py
└── README.md
```

---

## How to Run

Run the program:

```bash
python linked_list.py
```

Run tests:

```bash
python -m unittest
```

Or:

```bash
python -m unittest test_linked_list.py
```

---

## Example

```python
ll = LinkedList()

ll.insert_at_front(10)
ll.insert_at_front(20)
ll.insert_at_end(5)

print(ll.recursive_sum())       # 35
print(ll.recursive_search(10))  # True

ll.recursive_reverse()
```

---

## Concepts Practiced

* Linked Lists
* Recursion
* Node Traversal
* Recursive Base Cases
* Recursive Pointer Manipulation
* Object-Oriented Programming (OOP)

---

## Author

Steven Rouse
