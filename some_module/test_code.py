import numpy as np
import pytest

#### testing zero case ####
from some_module import integrate_trapz


def test_trapz():
    xs, ys = np.linspace(0, 10, 10), np.zeros(10)
    assert integrate_trapz(xs, ys) == 0

