from collections import deque


def is_palindrome(word: str)->bool:
    word = ''.join(word.lower().split())
    palindorme_deque = deque(word)
    while len(palindorme_deque) > 1:
        if palindorme_deque.pop() != palindorme_deque.popleft():
            return False
    
    return True
words = ['hello', 'this is palindrome', 'bob', 'level','palindromemordnilap']

for word in words:
    if is_palindrome(word):
        print(f"Word `{word}` is palindrome")
    else:
        print(f"Word `{word}` is not palindrome")