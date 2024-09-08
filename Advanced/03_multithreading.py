# 03_multithreading.py

# This script demonstrates basic multithreading in Python using the threading module.

import threading
import time

def print_numbers():
    """Function to print numbers from 1 to 5 with a delay."""
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

def print_letters():
    """Function to print letters from A to E with a delay."""
    for letter in 'ABCDE':
        print("Letter:", letter)
        time.sleep(1)

def main():
    # Create threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
