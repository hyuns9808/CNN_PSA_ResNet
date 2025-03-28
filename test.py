# https://build.nvidia.com/deepseek-ai/deepseek-r1-distill-qwen-32b?hosted_api=true
import numpy as np

strings = ["1.123451267e-5", "2.123451267e-3", "3.123451267e-7"]

# Parse each string
parsed = []
min_exponent = None

for s in strings:
    parts = s.split('e')
    significand = parts[0]
    exponent = int(parts[1])
    value = np.float64(s)
    parsed.append( (value, exponent) )
    if min_exponent is None or exponent < min_exponent:
        min_exponent = exponent

# Now scale each value
scaled_values = []
for value, exponent in parsed:
    scale_factor = 10 ** (-min_exponent) 
    scaled = value * scale_factor
    scaled_values.append( scaled )

# Convert to float32
result = np.array(scaled_values, dtype=np.float32)

print(result)