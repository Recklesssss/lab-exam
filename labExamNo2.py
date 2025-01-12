def compute_cross_product(a, b):
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Both vectors must have exactly 3 elements for a cross product.")
    
    cross_product = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]
    return cross_product

# Example usage
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
print("Cross Product:", compute_cross_product(vector_a, vector_b))  # Output: [-3, 6, -3]
