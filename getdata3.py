import requests
import os

# List of URLs to download
urls = [
    "https://chargeplacescotland.org/wp-content/uploads/2024/08/CPS-JULY-Sessions.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/08/JUNE-24-SESSIONS.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/06/MAY-24-SESSIONS-CLEAN.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/05/APR-24-SESSIONS-CLEAN.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/04/MARCH-24-sessions-CLEAN.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/04/Sessions-FEB-24-CLEAN.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/03/Sessions-JAN-24-CLEAN-1.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/01/Sessions-DEC-23.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2024/05/NOV-23-sessions-CLEAN-1.csv",
    "https://chargeplacescotland.org/wp-content/uploads/2023/12/Sessions-OCT-24.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/10/Public-Sessions-SEP-23.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/09/Public-Sessions-Website-AUG-23.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/08/SESSIONS-JULY-23.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/07/Sessions-JUNE-23.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/07/Sessions-PUBLIC.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/07/April-Sessions-PUBLIC.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/07/March-Public-Sessions.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/07/Public-Sessions-FEB-2023.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/07/JAN-23-Public-Sessions.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/11/Sessions-CSV-vlookup-DEC-22-1.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/07/November-Sessions.xlsx",
    "https://chargeplacescotland.org/wp-content/uploads/2023/12/October-Sessions.xlsx"
]

# Directory to save the downloaded files
download_dir = 'session_reports'
os.makedirs(download_dir, exist_ok=True)

# Download each file
for url in urls:
    file_name = os.path.basename(url)
    file_path = os.path.join(download_dir, file_name)
    
    # Download the file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    
    # Save the file
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    print(f"Downloaded {file_name}")

print("All specified files have been downloaded.")