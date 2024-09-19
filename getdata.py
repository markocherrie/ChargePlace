import requests
from bs4 import BeautifulSoup
import os

# URL of the webpage
url = "https://chargeplacescotland.org/monthly-charge-point-performance/"

# Fetch the webpage content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <a> tags with href attributes ending in .csv or xlsx
csv_links = soup.find_all('a', href=lambda href: href and (href.endswith('.csv') or href.endswith('.xlsx')))

# Directory to save the downloaded CSV files
download_dir = 'csv_reports'
os.makedirs(download_dir, exist_ok=True)

# Download each CSV file
for link in csv_links:
    csv_url = link['href']
    csv_name = os.path.basename(csv_url)
    csv_path = os.path.join(download_dir, csv_name)
    
    # Download the CSV file
    csv_response = requests.get(csv_url)
    csv_response.raise_for_status()  # Check if the request was successful
    
    # Save the CSV file
    with open(csv_path, 'wb') as file:
        file.write(csv_response.content)
    
    print(f"Downloaded {csv_name}")

print("All CSV files have been downloaded.")