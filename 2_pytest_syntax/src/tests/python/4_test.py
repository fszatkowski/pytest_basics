import pytest

""" 
If tests include floats, be aware of possible problems due to fixed precision of floating point arithmetics
For basic floats use pytest.approx, for matrix calculations, use np.testing module 
"""


def test_numeric_comp_fails():
    with pytest.raises(AssertionError):
        assert (0.2 + 0.1) == 0.3


def test_numeric_comp_correct():
    assert (0.2 + 0.1) == pytest.approx(0.3)
