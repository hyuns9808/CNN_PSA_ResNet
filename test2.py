import numpy as np

def convert_and_normalize(strings):
    # Parse strings to float64
    numbers = np.array([float(s) for s in strings], dtype=np.float64)
    
    # Extract exponents
    exponents = np.log10(np.abs(numbers))  # Get exponents as log10
    exponents = np.floor(exponents)  # Get the exponent part
    print(exponents)
    
    # Find the minimum exponent
    min_exp = np.min(exponents)
    
    # Normalize each number to min_exp
    scaling_factors = 10.0 ** (min_exp)
    normalized_numbers = numbers / scaling_factors
    
    # Convert to float32
    normalized_float32 = normalized_numbers.astype(np.float32)
    
    return normalized_float32

strings = ["1.123451267e-5", "2.123451267e-3", "3.123451267e-7"]
print(convert_and_normalize(strings))