# Geometric Sequence Triplets

A geometric sequence triplet is a **sequence of three numbers** where each successive number is obtained by multiplying the preceding number by a constant called the **common ratio**.

Let's examine `three` triplets to understand how this works:
- `(1, 2, 4)`: This is a geometric sequence with a ratio of `2 (i.e., [1, 1⋅2 = 2, 2⋅2 = 4])`.
- `(5, 15, 45)`: This is a geometric sequence with a ratio of `3 (i.e., [5, 5⋅3 = 15, 15⋅3 = 45])`.
- `(2, 3, 4)`: Not a geometric sequence.
Given an array of integers and a common ratio r, find all triplets of indexes `(i, j, k)` that follow a geometric sequence for `i < j < k`. It's possible to encounter duplicate triplets in the array.

**Example:**
```
Input: nums = [2, 1, 2, 4, 8, 8], r = 2
Output: 5
```
Explanation:
- Triplet `[2, 4, 8]` occurs at indexes `(0, 3, 4), (0, 3, 5), (2, 3, 4), (2, 3, 5)`.
- Triplet `[1, 2, 4]` occurs at indexes `(1, 2, 3)`.