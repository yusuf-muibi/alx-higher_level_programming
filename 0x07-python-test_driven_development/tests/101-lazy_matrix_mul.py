#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (list): The first matrix (list of lists).
        m_b (list): The second matrix (list of lists).

    Raises:
        ValueError: If m_a or m_b is not a list or not a list of lists.
        ValueError: If m_a or m_b is empty or not a rectangle, or if matrices can't be multiplied.

    Returns:
        np.ndarray: The result of matrix multiplication as a NumPy array.
    """
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.matmul(np_m_a, np_m_b)
        return result.tolist()
    except (ValueError, TypeError) as e:
        raise ValueError(str(e))
