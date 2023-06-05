def validate_brackets(str):
    """
    Validates if the brackets in a given string are balanced.

    Parameters:
    str: The input string to be checked for balanced brackets.

    Returns:
    bool: True if the brackets are balanced, False otherwise.
    """

    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for bracket in str:
        if bracket in brackets.keys():  # Opening bracket
            stack.append(bracket)
        elif bracket in brackets.values():  # Closing bracket
            if not stack or bracket != brackets[stack.pop()]:
                return False

    return len(stack) == 0
