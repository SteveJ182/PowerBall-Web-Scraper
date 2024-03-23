import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://nclottery.com/powerball-past-draws'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the link containing the CSV file
    csv_link = soup.find('a', string='here', href=True)
    
    # Extract the URL of the CSV file
    if csv_link:
        csv_url = 'https://nclottery.com' + csv_link['href']
        
        # Download the CSV file
        csv_response = requests.get(csv_url)
        
        # Check if the download was successful
        if csv_response.status_code == 200:
            # Save the CSV file
            with open('powerball_draws.csv', 'wb') as f:
                f.write(csv_response.content)
            print('CSV file downloaded successfully.')
        else:
            print('Failed to download the CSV file.')
    else:
        print('CSV link not found.')
else:
    print('Failed to fetch the webpage.')

