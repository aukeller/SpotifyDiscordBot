import os 

import discord
from playlistadd import Spotify

#TODO deploy to heroku, make sure environment vars can be accessed, add bot to channel

# Spotify Access & Refresh tokens, playlist id, client id & secret
SP_ACCESS_TOKEN = os.environ.get('SP_ACCESS_TOKEN')
SP_REFRESH_TOKEN = os.environ.get('SP_REFRESH_TOKEN')
SP_CLIENT_ID = os.environ.get('SP_CLIENT_ID')
SP_CLIENT_SECRET = os.environ.get('SP_CLIENT_SECRET')
PLAYLIST_ID = os.environ.get('PLAYLIST_ID')


# Discord Token 
DISC_TOKEN = os.environ.get('DISC_TOKEN')


# instantiates clients for both spotify & discord
spotify_client = Spotify(SP_ACCESS_TOKEN, SP_REFRESH_TOKEN, SP_CLIENT_ID, SP_CLIENT_SECRET)
disc_client = discord.Client()

spotify_track_url = 'https://open.spotify.com/track/'

# Check to see that discord client was set up properly and prints login message
@disc_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(disc_client))

@disc_client.event
async def on_message(message):
    # when message in channel contains url prefix, grab the uri and add it to the playlist
    if spotify_track_url in message.content:
        spotify_uri = 'spotify:track:' + message.content.split('track/')[1]
        spotify_uri = spotify_uri.split('?')[0]
        

        await spotify_client.playlist_add_items(PLAYLIST_ID, [spotify_uri])
        await message.channel.send('Added to playlist!')

disc_client.run(DISC_TOKEN)