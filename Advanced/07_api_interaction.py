# 07_api_interaction.py

# This script demonstrates how to interact with an API using the requests library.

import requests

def get_api_data(url):
    """Fetch data from an API endpoint."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def main():
    url = 'https://api.example.com/data'  # Replace with a real API endpoint
    data = get_api_data(url)
    
    # Print some data to verify
    print("API Data:")
    print(data)

if __name__ == "__main__":
    main()
