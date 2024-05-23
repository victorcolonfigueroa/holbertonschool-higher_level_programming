# Test with an empty list
my_list = MyList()
my_list.print_sorted()  # Expected output: []

# Test with a list containing one element
my_list = MyList([1])
my_list.print_sorted()  # Expected output: [1]

# Test with a list containing duplicates
my_list = MyList([3, 1, 2, 3])
my_list.print_sorted()  # Expected output: [1, 2, 3, 3]

# Test with an already sorted list
my_list = MyList([1, 2, 3])
my_list.print_sorted()  # Expected output: [1, 2, 3]

# Test with a reverse sorted list
my_list = MyList([3, 2, 1])
my_list.print_sorted()  # Expected output: [1, 2, 3]

# Test with a list with different data types (integers and floats)
my_list = MyList([1, 2.5, 2])
my_list.print_sorted()  # Expected output: [1, 2, 2.5]

# Test with a list containing strings
my_list = MyList(["banana", "apple", "cherry"])
my_list.print_sorted()  # Expected output: ['apple', 'banana', 'cherry']

# Test with a list with mixed data types (integers and strings)
my_list = MyList([1, "apple", 3])
try:
    my_list.print_sorted()  # This should raise a TypeError
except TypeError as e:
    print(f"Error: {e}")

# Test with a subclass of list
class CustomList(list):
    pass

custom_list = CustomList([3, 1, 2])
my_list = MyList(custom_list)
my_list.print_sorted()  # Expected output: [1, 2, 3]
