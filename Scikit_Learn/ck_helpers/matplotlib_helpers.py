import numpy as np
import matplotlib.pyplot as plt
from typing import *

def simple_plot(X:np.ndarray, Y:np.ndarray, X_label:Optional[str] = None, Y_label:Optional[str] = None):
    plt.plot(X, Y)

    if (X_label is not None and len(X_label) > 0):
        plt.xlabel(X_label)

    if (Y_label is not None and len(Y_label) > 0):
        plt.ylabel(Y_label)

    plt.show()