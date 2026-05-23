# Day 5 – LU Decomposition

**Date:** 2026-05-22

## Topics Covered
- Doolittle LU decomposition (no pivoting) for square matrices
- Forward and back substitution to solve `Ax = b`
- Verification of `A = L @ U`
- Comparison with `scipy.linalg.lu` (partial pivoting)

## Files Created
- `notebooks/05_LU_Decomposition.ipynb` – Full notebook with theory, implementation, tests, and limitations

## Key Learnings
- `L` unit lower triangular, `U` upper triangular
- Formulas derived from equating `A = L U`
- Forward/back substitution reuses triangular structure
- Zero pivot or near‑zero pivot can cause failure (discussed)

## Example Tested
- 3×3 and 5×5 matrices; solutions validated with `np.linalg.solve`

