# Verification 1: A * inv(A) should be identity
identity_check = A @ invA
print("\nVerification A @ inv(A) ≈ I:\n", identity_check)
print("Is close to identity?", np.allclose(identity_check, np.eye(rows)))

# Verification 2: First eigenpair
v0 = eigvecs[:, 0]
λ0 = eigvals[0]
left = A @ v0
right = λ0 * v0
print("\nFirst eigenvector v0:", v0)
print("A @ v0:", left)
print("λ0 * v0:", right)
print("Eigenvalue equation holds?", np.allclose(left, right))