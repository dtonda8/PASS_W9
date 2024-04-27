# PASS_W9
No in-builts allowed :)

### Q1: Power of Four 
Given an integer `n`, return true if it is a power of four (without using the `log` function). Otherwise, return false.

An integer `n` is a power of four, if there exists an integer x such that `n` == $4^x$.

Example 1:
**Input**: n = 64  
**Output**: true  
Explanation: 64 = $4^3$

Example 2:  
**Input**: n = 0  
**Output**: false  
Explanation: There is no x where $4^x$ = 0.

Example 3:  
**Input**: n = -1  
**Output**: false  
Explanation: There is no x where $4^x$ = -1.

Extra: if you done the iterative approach, try the recursive approach (or vice versa)

---

### Q2: Merge 2 Sorted Lists 
You are given the heads of two lists `list1` and `list2`, that are already sorted.

Merge the two lists into one sorted list, and return the merged list. Aim to do this within $O(n)$.

Try using the recursive approach (create aux function), if stuck you can try the iterative approach first.

Example 1:  
**Input**: `list1` = [1,2,4], `list2` = [1,3,4]  
**Output**: [1,1,2,3,4,4]  

Example 2:  
**Input**: `list1` = [1,4,6,7,11], `list2` = [5,9]  
**Output**: [1,4,5,6,7,9,11]  

Example 3:  
**Input**: `list1` = [], `list2` = []  
**Output**: []  

---

### Testing you algorithm
- To run tests, open terminal then:
```sh
python3 run_tests.py # and follow command line instructions
```

- If you encounter errors with the above, make sure that at least python runs on terminal
```sh
python3
```

- You may be directed to Microsoft Store (Windows), if so install python from there
- For if issues persist on Mac,  see this: https://docs.python-guide.org/starting/install3/osx/
