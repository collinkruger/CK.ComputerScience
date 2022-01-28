import numpy as np
from ck_python_helpers import *


def display_head(arr: np.ndarray, count:int = 10) -> None:

    ValidateArgumentType("arr", np.ndarray, False, arr)
    ValidateArgumentType("count", int, False, count)

    display(arr[:count])


def display_tail(arr: np.ndarray, count:int = 10) -> None:

    ValidateArgumentType("arr", np.ndarray, False, arr)
    ValidateArgumentType("count", int, False, count)

    display(arr[count:])