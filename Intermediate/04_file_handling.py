# 04_file_handling.py

# This script demonstrates how to handle files in Python.

def read_file(file_path):
    """Function to read the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found."

def write_file(file_path, content):
    """Function to write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}")

def main():
    # Define file paths
    read_path = 'example_read.txt'
    write_path = 'example_write.txt'
    
    # Write to a file
    write_file(write_path, "This is a test file.")

    # Read from a file
    file_content = read_file(write_path)
    print("File content:")
    print(file_content)

if __name__ == "__main__":
    main()
