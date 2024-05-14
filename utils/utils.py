# Function to convert string values to float
def normalize_array(array: list) -> list:
    for i, value in enumerate(array):
        if i == 0:
            continue
        else:
            array[i] = float(array[i])
    return array
