# Day 2 – NumPy linalg

**Date:** 2026-05-19

## Topics Covered
- Random matrix generation (uniform, normal, discrete, complex)
- Reproducibility with seeds
- Symmetric & Hermitian matrices
- Determinant, inverse, eigenvalues (with verification)
- Singularity check with tolerance

## Files Created
- `notebooks/02_numpy_linalg_basics.ipynb` – Full notebook with theory and code
- `src/linalg_utils.py` (optional – you can extract functions later)

## Key Learnings
- Broadcasting rules for matrix addition
- Matrix multiplication inner dimension constraint
- Transpose properties (including `(AB)^T = B^T A^T`)
- Floating‑point tolerance for singularity (`abs(det) < 1e-10`)

## Verification
- Checked `A @ inv(A) ≈ I` using `np.allclose`
- Verified eigenvalue equation `A v ≈ λ v`
- Confirmed symmetric matrix yields real eigenvalues

