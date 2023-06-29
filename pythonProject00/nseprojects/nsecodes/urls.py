import requests
import json

url = "https://www.nseindia.com/api/..."
date = "2023-06-23"

response = requests.get(url)
data = json.loads(response.text)


# Process the retrieved data as per your requirements
