import numpy as np

def lu_decomposition(A):
    """
    Doolittle LU decomposition (no pivoting). Returns L (unit lower triangular)
    and U (upper triangular) such that A = L @ U.
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    
    for i in range(n):
        # Row i of U
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        # Column i of L
        for j in range(i+1, n):
            pivot = U[i, i]
            if pivot == 0:
                raise ValueError("Zero pivot encountered – try partial pivoting")
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / pivot
    
    return L, U

def forward_substitution(L, b):
    """Solve L y = b for y (L is unit lower triangular)."""
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    return y

def backward_substitution(U, y):
    """Solve U x = y for x (U is upper triangular)."""
    n = len(y)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        pivot = U[i, i]
        if pivot == 0:
            raise ValueError("Zero pivot in back substitution")
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / pivot
    return x

def solve_lu(A, b):
    """Solve Ax = b using LU decomposition (no pivoting)."""
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x
