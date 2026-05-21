# Day 3 – Vectors & Matrices (Visualisation)

**Date:** 2026-05-20

## Topics Covered
- Plotting 2D vectors with `matplotlib` arrows using `annotate` (stable for resizable figures)
- Vector addition (head‑to‑tail method) visualisation
- Scalar multiplication visualisation
- Orthogonality check via dot product with tolerance `1e-10`
- Vector projection: formula and geometric plot with dashed line from `v` tip to `proj` tip

## Files Created
- `notebooks/03_vectors_matrices.ipynb` – Full notebook with all code, markdown theory, and examples

## Key Learnings
- `plt.annotate` is superior to `plt.arrow` for dynamic figure sizes
- Head-to-tail addition: chain vectors and draw resultant from origin
- Projection formula: `proj = (v·u)/(u·u) * u`
- Dynamic axis scaling using `np.ptp` and padding
- Tolerance is essential for floating-point orthogonality checks

## Verification
- Orthogonal test: `[2,3]` and `[-3,2]` → `True`
- Projection of `[2,3]` onto `[4,1]` → `[2.588, 0.647]` (matches manual calculation)

## Next Up
Day 4: Pandas basics (Series, DataFrame, CSV I/O)
