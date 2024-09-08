# Advanced Python Programming

Welcome to the Advanced Python Programming section! This folder covers sophisticated topics and techniques that build on intermediate concepts. Explore advanced features of Python with detailed explanations and practical examples.

## Introduction to Advanced Concepts

In this advanced section, you'll explore:
- **Decorators**: Enhancing functions with additional behavior.
- **Generators**: Efficiently handling large datasets using iterators.
- **Multi-threading**: Executing multiple threads concurrently to optimize performance.
- **Context Managers**: Managing resources efficiently with `with` statements.
- **Web Scraping**: Extracting data from websites.
- **Data Analysis**: Processing and analyzing data with Python libraries.
- **API Interaction**: Communicating with web services and APIs.

## Advanced Concepts

### 1. Decorators

**File**: `01_decorators.py`

**Explanation**: Decorators are a powerful feature in Python that allow you to modify or enhance the behavior of functions or methods. They are often used to add functionality to existing code in a clean and readable way.

**Code Example**:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function.")
        result = func(*args, **kwargs)
        print("Something is happening after the function.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))
```
- **Output**:
  ```
  Something is happening before the function.
  Something is happening after the function.
  Hello, Alice!
  ```

**Concepts Covered**:
- **Creating Decorators**: Define a decorator function and apply it with `@decorator`.
- **Function Wrapping**: Adding behavior before and after function execution.

**Use Case**: Logging, performance measurement, and access control.

### 2. Generators

**File**: `02_generators.py`

**Explanation**: Generators are a type of iterable that allows you to iterate over a sequence of values efficiently. They are useful for handling large datasets or streams of data without loading everything into memory at once.

**Code Example**:
```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))
```
- **Output**:
  ```
  0
  1
  1
  2
  3
  5
  8
  13
  21
  34
  ```

**Concepts Covered**:
- **Creating Generators**: Use `yield` to produce values one at a time.
- **Iterating with Generators**: Efficiently process sequences of data.

**Use Case**: Reading large files, generating infinite sequences.

### 3. Multi-threading

**File**: `03_multithreading.py`

**Explanation**: Multi-threading allows you to run multiple threads concurrently, which is useful for I/O-bound tasks. This script demonstrates how to use Python's `threading` module to perform concurrent operations.

**Code Example**:
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to finish
thread1.join()
thread2.join()
```
- **Output**:
  - Numbers and letters will be printed concurrently, demonstrating parallel execution.

**Concepts Covered**:
- **Creating Threads**: Use `threading.Thread` to run tasks in parallel.
- **Concurrency**: Improve performance by running multiple tasks simultaneously.

**Use Case**: Network requests, file I/O operations.

### 4. Context Managers

**File**: `04_context_managers.py`

**Explanation**: Context managers handle resource management by automatically handling setup and teardown operations. They are commonly used with the `with` statement to manage resources like files and network connections.

**Code Example**:
```python
from contextlib import contextmanager

@contextmanager
def open_file(file_path):
    file = open(file_path, 'w')
    try:
        yield file
    finally:
        file.close()

# Using the context manager
with open_file('example.txt') as file:
    file.write('Hello, context manager!')
```
- **Output**:
  - The file `example.txt` will contain the text "Hello, context manager!".

**Concepts Covered**:
- **Creating Context Managers**: Manage resources with `@contextmanager`.
- **Resource Management**: Ensure resources are properly closed or released.

**Use Case**: File operations, database connections.

### 5. Web Scraping

**File**: `05_web_scraping.py`

**Explanation**: Web scraping involves extracting data from websites. This script uses libraries like `requests` and `BeautifulSoup` to fetch and parse HTML content from web pages.

**Code Example**:
```python
import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

# Example usage
url = 'https://www.example.com'
print(fetch_title(url))
```
- **Output**:
  - The title of the webpage specified by the URL.

**Concepts Covered**:
- **Making HTTP Requests**: Fetch web content with `requests`.
- **Parsing HTML**: Extract data using `BeautifulSoup`.

**Use Case**: Data extraction, monitoring website content.

### 6. Data Analysis

**File**: `06_data_analysis.py`

**Explanation**: Data analysis involves processing and analyzing data to gain insights. This script uses libraries like `pandas` and `numpy` to perform data manipulation and analysis.

**Code Example**:
```python
import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'Salary': [50000, 60000, 55000]
}
df = pd.DataFrame(data)

# Performing analysis
mean_salary = np.mean(df['Salary'])
print(f"Mean Salary: {mean_salary}")

# Filtering data
filtered_df = df[df['Age'] > 23]
print(filtered_df)
```
- **Output**:
  ```
  Mean Salary: 55000.0
      Name  Age  Salary
  0  Alice   24   50000
  1    Bob   27   60000
  ```

**Concepts Covered**:
- **Data Manipulation**: Handle and process data with `pandas`.
- **Statistical Analysis**: Compute statistics and filter data.

**Use Case**: Data cleaning, statistical analysis.

### 7. API Interaction

**File**: `07_api_interaction.py`

**Explanation**: Interacting with APIs involves sending requests to and processing responses from web services. This script demonstrates how to make API requests and handle JSON data using Python.

**Code Example**:
```python
import requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['weather'][0]['description']

# Example usage
api_key = 'your_api_key'
city = 'London'
print(get_weather(api_key, city))
```
- **Output**:
  - The weather description for the specified city.

**Concepts Covered**:
- **Making API Requests**: Use `requests` to communicate with web APIs.
- **Handling JSON**: Parse and extract information from JSON responses.

**Use Case**: Fetching data from web services, integrating external data.

## Conclusion

The advanced section of Python programming provides deeper insights and tools to handle complex tasks efficiently. Mastery of these concepts will prepare you for challenging projects and real-world applications. For further learning, consider exploring specialized resources or engaging with the Python community.

Happy coding!
```

This `README.md` file includes detailed explanations, code examples, and use cases for each topic in the `advanced` folder, helping users understand and apply these advanced Python concepts effectively. Feel free to adjust or expand the content to fit your specific needs.
