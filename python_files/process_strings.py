import re

"""
Function that reads a file containing two columns (time, current values).
Returns two lists: times and currents, saved as raw strings
Inputs:
    1) file_path: directory path of file that is going to be split
Returns:
    1) times: STRING array of time values
    2) currents: STRING array of current values
"""
def read_file_string(file_path):
    times = []
    currents = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.split()
            if len(values) == 2:
                times.append(values[0])
                currents.append(values[1])
    return times, currents

''' 
Function that strips trace values from exponent values, return stripped values and avg e value
Inputs:
    1) current: raw value array (looks like 4.23623807e-03)
Returns:
    1) result: stripped value(4.23623807) array; STRING array
    2) e_val: stripped exponent value(-3) array; STRING array
'''
def strip_and_get_exp(current):
    result = []
    e_val = []
    # First iteration: go through all values, strip with value and e value, get avg e value
    for value in current:
        # Edge case: value is "-0.00000000e+00" or "0.00000000e+00"
        # Add more edge cases if needed
        if value in ["-0.00000000e+00", "0.00000000e+00"]:
            # append string to result, int to e_val
            result.append('0')
            e_val.append(0)
        else:
            try:
                match = re.search(r"(?<=e-)\d+", value)
                if match:
                    if value[0] == "-":
                        strip_val = value[0:11]
                        strip_val_e = value[12:15]
                    else:
                        strip_val = value[0:10]
                        strip_val_e = value[11:14]
                    # value must be remained as string
                    result.append(strip_val)
                    # e_val casted to string to get avg
                    e_val.append(int(strip_val_e))
                    '''
                    # Debugging scripts; do not erase
                    print(f"\tstrip_val: {strip_val}")
                    print(f"\tstrip_val_e: {strip_val_e}\n")
                    new_val = process_string(strip_val, strip_val_e)
                    print(f"\tProcessed: {new_val}")
                    print(f"\tFloat32 of processed: {np.float32(new_val)}\n")
                    '''
            except ValueError as e:
                print(f"Error parsing value '{value}': {e}")
    return result, e_val

