def next_lexicographical_sequence(st):
    letters = list(st)
    pivot = len(st) - 2

    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1
    
    if pivot == -1:
        return "".join(reversed(letters))
    
    rightmost_successor = len(st) - 1
    while letters[rightmost_successor] <= letters[pivot]:
        rightmost_successor -= 1
    
    letters[pivot], letters[rightmost_successor] = letters[rightmost_successor], letters[pivot]

    letters[pivot + 1:] = reversed(letters[pivot + 1:])

    return "".join(letters)

st = input().strip()
next_lexicographical = next_lexicographical_sequence(st)
print(next_lexicographical)