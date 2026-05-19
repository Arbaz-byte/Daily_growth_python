# Day 1 – Python & NumPy Essentials

**Date:** 2026-05-18

## Topics Covered
- Vector and 2×3 matrix creation
- Dot product (manual loop, `np.dot`, `@` operator)
- Euclidean distance (manual loop with NumPy)
- Cramer's rule for n×n systems

## Files Created
- `notebooks/01_python_numpy_essentials.ipynb` – Main notebook with all code and explanations
- `src/utils.py` – Reusable Cramer's rule function

## Example Outputs
- Dot product of `[4,5,6]` and `[8,9,6]` = 113
- Euclidean distance between `[1,2]` and `[4,6]` = 5.0
- Cramer's rule solves 2×2 and 5×5 systems correctly

## Verification
All results match NumPy's built‑in functions (`np.dot`, `np.linalg.norm`, `np.linalg.solve`).

## Next Up
Day 2: Pandas basics + data visualization
