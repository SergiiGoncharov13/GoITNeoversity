from collections import deque

text = input("Type your palindrome here >  ")

def user_string(text):
    p_srting = ''.join(ch.lower() for ch in text if ch.isalpha())
    deque_p = deque(p_srting)
    return deque_p

def polindron(deque_p):
    while len(deque_p) > 1:
        if deque_p.popleft() != deque_p.pop():           
            return print("False")
    return print("True")



polindron(user_string(text))



