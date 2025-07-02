# Verify Sudoku Board

Given a partially completed 9×9 Sudoku board, determine if the current state of the board adheres to the rules of the game:
- Each **row** and **column** must contain unique numbers between 1 and 9, or be empty (represented as 0).
- Each of the nine 3×3 **subgrids** that compose the grid must contain unique numbers between 1 and 9, or be empty.

Note: You are asked to determine whether the **current state of the board** is valid given these rules, **not** whether the board is solvable.

**Example:**
```
Input: board = [[3,0,6,0,5,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[1,0,2,5,0,0,3,2,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[0,1,0,0,0,0,0,7,4],[0,3,0,0,0,8,2,5,0],[0,0,5,2,0,6,0,0,0]]
Output: False
```

**Constraints:**
- Assume each integer on the board falls in the range of `[0, 9]`.