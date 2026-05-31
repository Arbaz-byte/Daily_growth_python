Day 7 - SVD & PCA + Consolidation (Completed)

**Date:** 2026-05-31
**Status:** ✅ Notebook completed and committed.

# Completed Tasks (implemented in `07_svd_image_compression.ipynb`)

- [x] Load a grayscale image (e.g., using `plt.imread` or `skimage.data.camera()`).
- [x] Perform truncated Singular Value Decomposition (SVD) on the image matrix.
- [x] Reconstruct the image using ranks 5, 20, and 50.
- [x] Display original and reconstructed images side-by-side.
- [x] Write a markdown cell explaining compression ratio vs. image quality trade-off.
-

# Reflection
The SVD & PCA topic required a solid grasp of linear algebra fundamentals. By taking the time to understand the mathematics behind truncation and reconstruction, the implementation became clear. The trade-off between compression ratio and image quality is evident: low ranks (e.g., 5) produce blocky, lossy results but save significant space, while rank 50 preserves most details with moderate compression.

# Completion Log
Notebook finalized and pushed on **2026-05-31**. The 7-day sprint concluded successfully.
