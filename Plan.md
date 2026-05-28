# Week 1 plan 

**7-Day Recovery Sprint | Linear Algebra | Code GitHub**

---

## Day 1:- Python + NumPy essentials  
**Notebook:** `01_python_numpy_essentials.ipynb`

### Tasks:
- [ ] Open Jupyter, follow the NumPy Quickstart typing every line yourself.
- [ ] Create a vector (`np.array([1,2,3])`), a $2\times3$ matrix.
- [ ] Compute dot product of two vectors.
- [ ] Write a function that returns the Euclidean distance between two vectors (using a for loop or NumPy sum).
- [ ] (If time) Solve a $2\times2$ system with Cramer's rule.

---

## Day 2:- NumPy linalg  
**Notebook:** `02_numpy_linalg_basics.ipynb`

### Tasks:
- [ ] Create random matrices; add, multiply, transpose.
- [ ] Use `np.linalg.det`, `np.linalg.inv`, `np.linalg.eig` on a symmetric matrix.
- [ ] Write a function `is_singular(A)` that returns True if determinant near zero.
- [ ] Write Cramer's rule solver for $2\times2$ as a function.

---

## Day 3: - Vectors & Matrices (from playlist) 
**Notebook:** `03_vectors_matrices.ipynb`

### Tasks:
- [ ] Create 2D vectors, plot them with matplotlib arrows.
- [ ] Visualise vector addition & scalar multiplication.
- [ ] Write `are_orthogonal(v1, v2)`.
- [ ] Implement vector projection: proj of v onto u, plot it.

---

## Day 4:- Gaussian Elimination  
**Notebook:** `04_gaussian_elimination.ipynb`

### Tasks:
- [ ] Write `gaussian_elimination(A, b)` that prints each step (row operations). Use $3\times3$ example.
- [ ] Test on $x+y+z=6$, $2y+5z=-4$, $2x+5y-z=27$.
- [ ] Compare with `np.linalg.solve`.
- [ ] (Bonus) Add back-substitution.

---

## Day 5: - LU Decomposition  
**Notebook:** `05_lu_decomposition.ipynb`

### Tasks:
- [ ] Implement `lu_decomposition(A)` for $3\times3$ without pivoting, return L, U.
- [ ] Verify $L \cdot U \approx A$
- [ ] Compare with `scipy.linalg.lu`.
- [ ] Write a markdown cell explaining the algorithm.


---

## Day 6:- Eigenvalues & Eigenvectors  
**Notebook:** `06_eigenvalues.ipynb`

### Tasks:
- [ ] Compute eigenvalues/vectors of a random symmetric matrix.
- [ ] Write `verify_eigen(A)` that checks $Av_{i}=\lambda_{i}v_{i}$ for all pairs, with tolerance.
- [ ] Diagonalise: $P^{-1}AP=D$, verify.
- [ ] Plot eigenvectors as axes of a transformed circle.

---

## Day 7:- SVD & PCA + Consolidation  
**Notebook:** `07_svd_image_compression.ipynb`

### Tasks:
- [ ] Load a grayscale image (use `plt.imread` or `skimage.data.camera()`).
- [ ] Perform truncated SVD, reconstruct with ranks 5, 20, 50; plot side-by-side.
- [ ] Write a markdown cell about compression ratio vs quality.
