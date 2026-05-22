import numpy as np

def row_echelon_form(A, b):
    """
    Perform Gaussian elimination to convert [A|b] to row echelon form.
    
    Parameters:
    A : numpy array (n x n) - Coefficient matrix
    b : numpy array (n,) - Right-hand side vector
    
    Returns:
    M : numpy array (n x n+1) - Augmented matrix in row echelon form
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Coefficient matrix must be square")
    if A.shape[1] != b.shape[0]:
        raise ValueError("Dimensions of A and b must match")
    
    M = np.column_stack((A.astype(float), b.astype(float)))
    n = len(b)
    all_col_zero = False
    
    for i in range(n):
        # Pivot search with partial pivoting (swap if zero)
        if M[i, i] == 0:
            for j in range(i+1, n):
                if M[j, i] != 0:
                    M[[i, j]] = M[[j, i]]
                    break
            else:
                all_col_zero = True
        
        if not all_col_zero:
            pivot = M[i, i]
            for j in range(i+1, n):
                factor = M[j, i] / pivot
                M[j] = M[j] - factor * M[i]
        else:
            raise ValueError("Columns are linearly dependent – no unique solution")
    
    return M

def back_substitution(M):
    """
    Perform back substitution on an upper triangular augmented matrix.
    
    Parameters:
    M : numpy array (n x n+1) - Augmented matrix in row echelon form
    
    Returns:
    solution : numpy array (n,) - Solution vector
    """
    n = M.shape[1] - 1
    solution = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        constant = M[i, -1]
        known_sum = np.sum(M[i, i+1:n] * solution[i+1:n])
        pivot_coeff = M[i, i]
        solution[i] = (constant - known_sum) / pivot_coeff
    
    return solution

def gaussian_elimination_solve(A, b):
    """
    Solve Ax = b using Gaussian elimination with back substitution.
    
    Returns:
    solution : numpy array (n,)
    """
    M = row_echelon_form(A, b)
    return back_substitution(M)
