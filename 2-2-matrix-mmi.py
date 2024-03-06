import numpy as np

def matrix_inverse(matrix, mod):
    # Use numpy to calculate the matrix inverse
    matrix = np.array(matrix)
    det = int(round(np.linalg.det(matrix)))
    
    # Check if the determinant is invertible (not divisible by the modulus)
    if np.gcd(det, mod) != 1:
        raise ValueError("Matrix is not invertible under the given modulus.")

    # Calculate the modular multiplicative inverse of the determinant
    det_inverse = pow(det, -1, mod)
    
    # Calculate the adjugate matrix
    adjugate_matrix = (det * np.linalg.inv(matrix)).round() % mod
    
    # Calculate the modular multiplicative inverse of the matrix
    inverse_matrix = (det_inverse * adjugate_matrix) % mod
    
    return inverse_matrix.astype(int)

def input_matrix(order):
    # Input the matrix elements row-wise
    matrix = []
    print("Enter the matrix elements row-wise:")
    for i in range(order):
        row = list(map(int, input().split()))
        if len(row) != order:
            raise ValueError("Invalid input. Please enter a row with {} elements.".format(order))
        matrix.append(row)
    return matrix

def main():
    try:
        # Input order of the matrix
        order = int(input("Enter the order of the square matrix: "))
        
        # Input the matrix elements
        matrix = input_matrix(order)
        
        # Input modulus value
        mod = int(input("Enter the modulus value: "))
        
        # Calculate the modular multiplicative inverse
        inverse_matrix = matrix_inverse(matrix, mod)
        
        # Print the result
        print("\nModular Multiplicative Inverse:")
        for row in inverse_matrix:
            print(" ".join(map(str, row)))

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
