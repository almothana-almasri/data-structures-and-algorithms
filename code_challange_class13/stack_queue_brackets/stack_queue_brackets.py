from code_challange_class13.stack_queue_brackets.stack_and_queue import Stack

def validate_brackets(str):
    """
    Validates if the brackets in a given string are balanced.

    Parameters:
    str: The input string to be checked for balanced brackets.

    Returns:
    bool: True if the brackets are balanced, False otherwise.
    """

    stack = Stack()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for bracket in str:
        if bracket in brackets.keys():  # Opening bracket
            stack.push(bracket)
        elif bracket in brackets.values():  # Closing bracket
            if stack.is_empty() or bracket != brackets[stack.pop()]:
                return False

    return stack.is_empty()
