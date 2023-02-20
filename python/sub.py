

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
    
    # Create a flow object
flow = InstalledAppFlow.from_client_secrets_file('client_secret.json',
                                                    scopes=['https://studio.youtube.com/channel/UCWUw5qxBTQExORiRr7S0z7Q'])
    
    # Get credentials and create an API client
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)
    
    # Get the list of subscribers
subscribers = youtube.subscriptions().list(
    part="snippet",
    mine=True
).execute()
    
    # Loop through the subscribers and print out the names
for subscriber in subscribers['items']:
    print(subscriber['snippet']['title'])