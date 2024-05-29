import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Read the CSV file and convert each row into a dictionary
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries using the json module
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
