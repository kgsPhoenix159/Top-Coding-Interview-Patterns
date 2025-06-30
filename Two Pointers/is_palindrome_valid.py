def is_palindrome_valid(st):
    left = 0
    right = len(st) - 1
    while left < right:
        while left < right and not st[left].isalnum():
            left += 1
        while left < right and not st[right].isalnum():
            right -= 1
        if st[left] == st[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

st = input().strip()
is_palindrome = is_palindrome_valid(st)
print(is_palindrome)