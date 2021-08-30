from stack import Stack

def reverse_string(string):
    if string is None:
        return 'Invalid input'
    elif len(string) == 0:
        return 'Invalid input'

    stack = Stack()
    res = []
    for char in string:
        stack.push(char)
    
    for _ in range(stack.size):
        res.append(stack.pop())
    
    return ''.join(res)

# print(reverse_string('abcd'))
# print(reverse_string('le duc duy'))
# print(reverse_string(''))
# print(reverse_string(None))

def balanced_expression(expression):
    stack = Stack()
    
    for char in expression:
        if is_left_bracket(char):
            stack.push(char)
        elif is_right_bracket(char):
            if stack.peek() == 'Stack is empty':
                return False
            if not is_match_brackets(stack.pop(), char):
                return False
    
    return stack.is_empty()

# ? Helper method
def is_left_bracket(char):
    left_brackets = ['(', '<', '[', '{']
    return True if char in left_brackets else False

# ? Helper method
def is_right_bracket(char):
    right_brackets = [')', '>', ']', '}']
    return True if char in right_brackets else False

# ? Helper method
def is_match_brackets(left, right):
    left_brackets = ['(', '<', '[', '{']
    right_brackets = [')', '>', ']', '}']
    return True if left_brackets.index(left) == right_brackets.index(right) else False


print(balanced_expression('(1+2)'))
print(balanced_expression('(1+2)))'))
print(balanced_expression(')2+1('))
print(balanced_expression('(2)+(1('))
print(balanced_expression('(([1] + <2>))[a]'))
