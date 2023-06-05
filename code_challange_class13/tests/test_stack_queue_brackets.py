from code_challange_class13.stack_queue_brackets.stack_queue_brackets import validate_brackets
import pytest

@pytest.mark.parametrize("input_string, expected_result", [
    ("{}", True),
    ("{}(){}", True),
    ("()[[Extra Characters]]", True),
    ("(){}[[]]", True),
    ("{}{Code}[Fellows](())", True),
    ("[({}]", False),
    ("(](", False),
    ("{(})", False),
    ("{", False),
    (")", False),
    ("[}", False),
])
def test_validate_brackets(input_string, expected_result):
    assert validate_brackets(input_string) == expected_result
