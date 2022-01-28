from typing import *


def ValidateArgumentType(name:str, expected_type:type, optional:bool, value:Any) -> None:
    if (type(value) == expected_type):
        pass
    elif (optional and value is None):
        pass
    else:
        raise ValueError(f"A {type(value).__name__} was supplied to {name} with value {value}, but {name} must be supplied a {f'Optional[{type}]' if optional else expected_type.__name__}.")