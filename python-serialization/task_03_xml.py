import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename for the output XML file.
    """
    root = ET.Element("data")
    
    def build_tree(element, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(element, key)
                build_tree(child, value)
        else:
            element.text = str(data)
    
    build_tree(root, dictionary)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.
    
    Args:
        filename (str): The filename of the input XML file.
        
    Returns:
        dict: The deserialized dictionary.
    """
    def parse_element(element):
        parsed_data = {}
        for child in element:
            if len(child):
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data
    
    tree = ET.parse(filename)
    root = tree.getroot()
    
    return parse_element(root)

# Example usage
if __name__ == "__main__":
    sample_dict = {
        'person': {
            'name': 'John',
            'age': '30',
            'is_student': 'false'
        },
        'address': {
            'street': '123 Main St',
            'city': 'Anytown'
        }
    }
    
    serialize_to_xml(sample_dict, 'output.xml')
    deserialized_dict = deserialize_from_xml('output.xml')
    
    print(deserialized_dict)
