import math

import numpy as np

from ck_numpy_helpers import *


#%%

def _DataGeneratorCore(source: np.ndarray,
                       number_of_elements: Optional[int],
                       random_state: Optional[int])\
                       -> Tuple[np.ndarray, np.ndarray]:

    ValidateArgumentType("source", np.ndarray, False, source)
    ValidateArgumentType("number_of_elements", int, True, number_of_elements)
    ValidateArgumentType("random_state", int, True, random_state)

    if (number_of_elements is not None and number_of_elements < 1):
        raise ValueError("number_of_elements must be None or greater than zero")

    else:
        repetitions = 1 if number_of_elements is None else math.ceil(number_of_elements / len(source))
        source_extended = np.tile(source, (repetitions, 1))

        maybe_shuffle(source_extended, random_state)

        subset = source_extended[:number_of_elements]

        return (subset[:, :-1],
                subset[:, -1])


#%%

def AND(number_of_elements: Optional[int] = None, random_state: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    :param number_of_elements: An optional int to limit or extend the number of elements returned. If number_of_elements is greater than the length of the source truth table, the truth table is repeated, then limited in length to match number_of_elements. If number_of_elements is None or is not supplied, all rows from the source truth table are returned.
    :param random_state: An optional int to be used when shuffling the source truth table. If random_state is None or is not supplied, the source truth table will NOT be shuffled.
    :return: An NDArray of rows from an AND truth table
    """
    source = np.array([[0, 0, 0],
                       [1, 0, 0],
                       [0, 1, 0],
                       [1, 1, 1]])

    return _DataGeneratorCore(source=source,
                              number_of_elements=number_of_elements,
                              random_state=random_state)


#%%

def OR(number_of_elements: Optional[int] = None, random_state: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    :param number_of_elements: An optional int to limit or extend the number of elements returned. If number_of_elements is greater than the length of the source truth table, the truth table is repeated, then limited in length to match number_of_elements. If number_of_elements is None or is not supplied, all rows from the source truth table are returned.
    :param random_state: An optional int to be used when shuffling the source truth table. If random_state is None or is not supplied, the source truth table will NOT be shuffled.
    :return: An NDArray of rows from an OR truth table
    """
    source = np.array([[0, 0, 0],
                       [1, 0, 1],
                       [0, 1, 1],
                       [1, 1, 1]])

    return _DataGeneratorCore(source=source,
                              number_of_elements=number_of_elements,
                              random_state=random_state)


#%%

def XOR(number_of_elements: Optional[int] = None, random_state: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    :param number_of_elements: An optional int to limit or extend the number of elements returned. If number_of_elements is greater than the length of the source truth table, the truth table is repeated, then limited in length to match number_of_elements. If number_of_elements is None or is not supplied, all rows from the source truth table are returned.
    :param random_state: An optional int to be used when shuffling the source truth table. If random_state is None or is not supplied, the source truth table will NOT be shuffled.
    :return: An NDArray of rows from an XOR truth table
    """
    source = np.array([[0, 0, 0],
                       [1, 0, 1],
                       [0, 1, 1],
                       [1, 1, 0]])

    return _DataGeneratorCore(source=source,
                              number_of_elements=number_of_elements,
                              random_state=random_state)


#%%

def SINEWAVE(steps: int = 360) -> Tuple[np.ndarray, np.ndarray]:

    ValidateArgumentType("steps", int, False, steps)
    if (steps < 1):
        raise ValueError(f"steps is expected to be greater than or equal to one, but was given {steps}.")

    X = np.linspace(0, 2 * np.pi, steps)
    Y = np.sin(X)

    return (X, Y)