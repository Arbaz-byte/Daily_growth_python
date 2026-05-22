# Day 4 – Gaussian Elimination

**Date:** 2026-05-21

## Topics Covered
- Gaussian elimination (row echelon form) with row operations
- Partial pivoting to avoid zero pivots
- Back substitution to solve upper triangular system
- Validation against `np.linalg.solve`

## Files Created
- `notebooks/04_gaussian_elimination.ipynb` – Notebook with implementation and testing

## Key Learnings
- How to form augmented matrix `[A|b]`
- Elementary row operations: swapping, scaling, elimination
- Forward elimination to create zeros below the diagonal
- Back substitution from bottom row upward
- Using `np.allclose` to compare floating-point solutions

## Example Tested
Linear System of equations:
$$
\begin{aligned}
x - 2y + 3z &= 9 \\
-x + 3y &= -4 \\
2x - 5y + 5z &= 17
\end{aligned}
$$

Solution matches `np.linalg.solve`.

