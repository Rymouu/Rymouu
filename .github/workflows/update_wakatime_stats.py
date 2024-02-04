import requests

WAKATIME_API_KEY = input("Enter Wakatime API Key: ")  # This will be injected through the GitHub Action

# Make API request to get coding stats
response = requests.get(f"https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={WAKATIME_API_KEY}")
data = response.json()

# Extract relevant information
total_seconds = data['data']['total_seconds']
hours = total_seconds / 3600

# Update README file with the stats
with open("README.md", "a") as readme:
    readme.write(f"**Last 7 days coding activity:** {round(hours, 2)} hours\n")
