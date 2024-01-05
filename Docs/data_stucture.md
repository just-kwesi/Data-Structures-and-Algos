# Data Structure

A data structure is a collections of values. An arrangement of data is also an explanations.  
Algorithm are the steps or process put into place to manipulate the values.  
*Data Structures + Algorithms = Programs*

## Data Strutures

### Arrays or Lists

Stores and organises items sequentially. Simple and very easy to use.

#### Operations

- lookup:   O(1)
- push:     O(1)
- insert:   O(n)
- delete:   O(n)

#### Types of arrays

- **Static Arrays:**
  - **Size:** The size of a static array is fixed and determined at compile-time.
  - **Memory Allocation:** Memory for a static array is allocated at the time of declaration and remains constant throughout the program's execution.  
  - **Usage:** Accessing and modifying elements in a static array is fast because the memory addresses are fixed.

- **Dynamic Arrays:**
  - **Size:** The size of a dynamic array can be changed during runtime.
  - **Memory Allocation:** Memory for a dynamic array is allocated during program execution using explicit allocation functions (e.g., `malloc` in C or `new` in C++).  
  - **Usage:** Dynamic arrays allow flexibility in terms of size, but accessing elements may be slightly slower due to the need to follow pointers.