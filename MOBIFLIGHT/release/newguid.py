#!python3

import uuid

# Function to generate a new GUID
def generate_guid():
    return str(uuid.uuid4())

# Input and output file paths
input_file = 'working.mcc'
output_file = 'out.mcc'

# Open the input file and the output file
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Read and process each line
    for line in infile:
        # Replace NEWGUID with a new GUID
        new_line = line.replace('NEWGUID', generate_guid())
        # Write the new line to the output file
        outfile.write(new_line)

print(f"Processing complete. The output has been saved to {output_file}.")
