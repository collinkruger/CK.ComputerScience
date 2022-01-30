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


def maybe_shuffle(arr: np.ndarray, random_state: Optional[int]) -> None:
    """
    :param arr: An NDArray
    :param random_state: An optional int for configuring how shuffle occurs. If random_state is set to None, then no shuffle will occur. For all other int values, random_state will be supplied to NumPy's underlying np.random.seed method before arr is shuffled.
    """

    ValidateArgumentType("arr", np.ndarray, False, arr)
    ValidateArgumentType("random_state", int, True, random_state)

    if (random_state is None):
        pass
    else:
        np.random.seed(random_state)
        np.random.shuffle(arr)