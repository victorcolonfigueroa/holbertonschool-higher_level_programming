import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data and save it to the specified file.

    Args:
        data (dict): A Python dictionary with data.
        filename (str): The filename of the output JSON file. If the output file already exists it should be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
