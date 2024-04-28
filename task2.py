from collections import deque

def is_palindrome(string):
    string = string.lower().replace(" ", "")
    char_queue = deque(string)
    
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

input_string = "aBb aa"
if is_palindrome(input_string):
    print(f"'{input_string}' є паліндромом.")
else:
    print(f"'{input_string}' не є паліндромом.")

input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f"'{input_string}' є паліндромом.")
else:
    print(f"'{input_string}' не є паліндромом.")
