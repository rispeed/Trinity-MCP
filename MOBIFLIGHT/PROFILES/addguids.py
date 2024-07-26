#!/usr/bin/python3
import xml.etree.ElementTree as ET
import uuid

# The path to the input file
input_file_path = 'NEW_CHALLENGER_WITH_EFISS-work2.mcc'
# Generate the output file path by appending '-fixed' before the file extension
output_file_path = input_file_path.rsplit('.', 1)[0] + '-fixed.' + input_file_path.rsplit('.', 1)[1]

# Function to create a new unique GUID
def generate_new_guid():
    return str(uuid.uuid4())

# Load and parse the XML file
tree = ET.parse(input_file_path)
root = tree.getroot()

# Function to process 'config' nodes within 'inputs' or 'outputs'
def process_configs(parent):
    for config in parent.findall('./config'):
        new_guid = None
        # Check if the 'guid' attribute exists and its value is 'noguid', then generate a new GUID
        if 'guid' in config.attrib and config.attrib['guid'] == 'noguid':
            new_guid = generate_new_guid()
            config.attrib['guid'] = new_guid
        
        # If there's a child <guid> element with text 'noguid', replace it with a new GUID
        for guid_element in config.findall('guid'):
            if guid_element.text == 'noguid':
                new_guid = new_guid or generate_new_guid()  # Generate if not already generated
                guid_element.text = new_guid
        
        # Process any <precondition> nodes within <settings> if the 'ref' attribute equals "noguid"
        for settings in config.findall('./settings'):
            for precondition in settings.findall('.//precondition'):
                if precondition.get('ref') == 'noguid':
                    precondition.set('ref', new_guid or generate_new_guid())  # Use config's new GUID

# Process 'config' nodes under both 'inputs' and 'outputs'
for inputs in root.findall('.//inputs'):
    process_configs(inputs)

for outputs in root.findall('.//outputs'):
    process_configs(outputs)

# Save the modified XML to a new file
tree.write(output_file_path)

print(f"File processed and saved as '{output_file_path}'.")
