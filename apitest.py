import requests
import time
import random
import json

def make_api_call_with_delay(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()  # Assuming the response is JSON data
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

# Base URL for Scryfall API
base_url = "https://api.scryfall.com/cards/search?q="

# Search query for the specific card "Flickerwisp" 
search_query = "Flickerwisp"

url = base_url + f'name:"{search_query}"'

# Make API call with random delay between 50ms and 100ms
delay = random.uniform(0.05, 0.1)
time.sleep(delay)
response_data = make_api_call_with_delay(url)
if response_data:
    # Pretty print the response data
    print(json.dumps(response_data, indent=4))  # Indent for readability