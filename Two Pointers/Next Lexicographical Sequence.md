# Next Lexicographical Sequence

Given a string of lowercase English letters, rearrange the characters to form a new string representing the **next immediate sequence in lexicographical** (alphabetical) **order**. If the given string is already last in lexicographical order among all possible arrangements, return the arrangement that's first in lexicographical order.

**Example 1:**
```
Input: st = 'abcd'
Output: 'abdc'
```
Explanation: `"abdc"` is the next sequence in lexicographical order after rearranging `"abcd"`.

**Example 2:**
```
Input: st = 'dcba'
Output: 'abcd'
```
Explanation: Since `"dcba"` is the last sequence in lexicographical order, we return the first sequence: `"abcd"`.

**Constraints:**
- The string contains at least one character.