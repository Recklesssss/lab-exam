def reconstruct_matrix(U, S, V):
    # Step 1: Expand S into a diagonal matrix
    rows, cols = len(U), len(V[0])
    S_matrix = [[0] * cols for _ in range(rows)]
    for i in range(min(len(S), rows, cols)):
        S_matrix[i][i] = S[i]
    
    # Step 2: Compute U * S
    US = [[sum(U[i][k] * S_matrix[k][j] for k in range(len(S_matrix[0]))) for j in range(len(S_matrix[0]))] for i in range(len(U))]
    
    # Step 3: Compute (U * S) * V^T
    V_T = [[V[j][i] for j in range(len(V))] for i in range(len(V[0]))]
    reconstructed_matrix = [[sum(US[i][k] * V_T[k][j] for k in range(len(V_T))) for j in range(len(V_T[0]))] for i in range(len(US))]
    
    return reconstructed_matrix

# Example usage
U = [[1, 0], [0, 1]]
S = [2, 3]
V = [[1, 0], [0, 1]]

print("Reconstructed Matrix:", reconstruct_matrix(U, S, V))
# Output: [[2, 0], [0, 3]]
