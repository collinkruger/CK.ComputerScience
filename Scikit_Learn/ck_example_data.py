import numpy as np
import math
from typing import *
from ck_python_helpers import *


#%%

def _DataGeneratorCore(source: np.ndarray,
                       number_of_elements: Optional[int],
                       random_state: Optional[int])\
                       -> np.ndarray:

    ValidateArgumentType("source", np.ndarray, False, source)
    ValidateArgumentType("number_of_elements", int, True, number_of_elements)
    ValidateArgumentType("random_state", int, True, random_state)

    if (number_of_elements is not None and number_of_elements < 1):
        raise ValueError("number_of_elements must be None or greater than zero")

    else:
        repetitions = 1 if number_of_elements is None else math.ceil(number_of_elements / len(source))
        source_extended = np.tile(source, (repetitions, 1))

        if (random_state is not None):
            np.random.seed(random_state)
            np.random.shuffle(source_extended)

        return source_extended[:number_of_elements]


#%%

def AND(number_of_elements:Optional[int] = None, random_state:Optional[int] = None) -> np.ndarray:
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

def OR(number_of_elements:Optional[int] = None, random_state:Optional[int] = None) -> np.ndarray:
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

def XOR(number_of_elements:Optional[int] = None, random_state:Optional[int] = None) -> np.ndarray:
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