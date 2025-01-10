import requests
from bs4 import BeautifulSoup
import pandas as pd

# --- Scrape and extract data ---
# Define the URL
url = "https://www.basketball-reference.com/teams/CHI/2025_games.html"

# Send a request and parse the HTML
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Failed to retrieve the webpage")
    exit()

# Locate the data table
table = soup.find('table', {'id': 'games'})  # 'games' is the table ID on Basketball-Reference

# Extract headers
headers = [th.text for th in table.find('thead').find_all('th')]
headers = headers[1:]  # Skip the first column ('Rk') which is redundant

# Extract rows of data
rows = table.find('tbody').find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    if cols:  # Avoid header or empty rows
        data.append([col.text for col in cols])

# Create a DataFrame
games_df = pd.DataFrame(data, columns=headers)

# Save or display the data
print(games_df.head())
games_df.to_csv('data/raw/chicago_bulls_game_stats.csv', index=False)

# --- Filter to Dosunmu's data ---
# Update the URL to Dosunmu's game logs
url = "https://www.basketball-reference.com/players/d/dosunay01/gamelog/2025"

# Request and parse the page
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Failed to retrieve the webpage")
    exit()

# Locate the player data table
table = soup.find('table', {'id': 'pgl_basic'})  # 'pgl_basic' is the table ID for player logs

# Extract headers
headers = [th.text for th in table.find('thead').find_all('th')]
headers = headers[1:]  # Skip the first column ('Rk')

# Extract rows of data
rows = table.find('tbody').find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    if cols:  # Avoid header or empty rows
        data.append([col.text for col in cols])

# Create a DataFrame
ayo_stats_df = pd.DataFrame(data, columns=headers)

# Display or save
print(ayo_stats_df.head())
ayo_stats_df.to_csv('data/raw/ayo_dosunmu_game_stats.csv', index=False)
