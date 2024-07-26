#!python
import sys
import uuid

def replace_noguid_with_guid(filename):
    # Generate a new unique GUID
    new_guid = str(uuid.uuid4())
    
    # Create the new filename by appending '-out' before the file extension
    new_filename = f"{filename.rsplit('.', 1)[0]}-out.{filename.rsplit('.', 1)[1]}"

    try:
        # Read the content of the original file
        with open(filename, 'r') as file:
            content = file.read()

        # Replace all instances of 'noguid' with the new GUID
        modified_content = content.replace('noguid', new_guid)

        # Write the modified content to the new file
        with open(new_filename, 'w') as file:
            file.write(modified_content)

        print(f"File processed successfully. Output saved to: {new_filename}")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        replace_noguid_with_guid(sys.argv[1])
