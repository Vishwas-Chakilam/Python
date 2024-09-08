# 04_context_managers.py

# This script demonstrates how to use context managers in Python.

class FileOpener:
    """A simple context manager for opening and closing files."""
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

def main():
    # Using the custom context manager to handle file operations
    with FileOpener('example_context.txt', 'w') as file:
        file.write("Hello, context manager!")

    # Reading the file to confirm content was written
    with FileOpener('example_context.txt', 'r') as file:
        content = file.read()
        print("File content:", content)

if __name__ == "__main__":
    main()
