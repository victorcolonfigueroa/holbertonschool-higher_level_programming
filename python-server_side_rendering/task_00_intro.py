import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Expected template to be a string, got {type(template)}")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Expected attendees to be a list of dictionaries, got {type(attendees)}")
        return
    
    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Using string replace method for substitution
        filled_template = template.replace("{name}", attendee.get('name', 'N/A'))
        filled_template = filled_template.replace("{event_title}", attendee.get('event_title', 'N/A'))
        filled_template = filled_template.replace("{event_date}", attendee.get('event_date', 'N/A'))
        filled_template = filled_template.replace("{event_location}", attendee.get('event_location', 'N/A'))
        
        output_filename = f"output_{index}.txt"
        
        try:
            # Check if file already exists
            if os.path.exists(output_filename):
                print(f"Warning: {output_filename} already exists and will be overwritten.")
            
            # Write the processed template to an output file
            with open(output_filename, "w") as file:
                file.write(filled_template)
        except Exception as e:
            print(f"An error occurred while writing {output_filename}: {e}")
