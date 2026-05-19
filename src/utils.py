import numpy as np

def cramers_compute(A, B):
    row, cols = A.shape
    if row != cols:
        return "Limitation Error: Cramer's rule works for square matrices only."
    elif A.size == 0 or B.size == 0:
        return "Error : Matrix is Empty"
    
    sol = []
    det = []
    D = np.linalg.det(A)
    
    if np.isclose(D, 0):
        return "No Unique Solution (No solution or Infinitely many solutions)"
    
    for i in range(row):
        copy_A = A.copy()
        copy_A[:, i] = B.flatten()
        det.append(round(np.linalg.det(copy_A)))
        sol.append(det[i] / D)
    
    sol_array = np.array(sol)
    det_array = np.array(det)
    
    return sol_array, det_array
