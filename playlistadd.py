import aiohttp
import time
import base64


class Spotify():
    # initializes with provided auth token, default url prefix for api requests, and headers
    def __init__(self, access_token, refresh_token, client_id, client_secret):
        
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

        self.expire_time = int(time.time()) + 3600
        self.url_prefix = "https://api.spotify.com/v1/"
        

    async def internal_call(self, url, payload):

        # creates dict for uri payload and adds playlist endpoint to url prefix    
        payload = {'uris': payload}
        url = self.url_prefix + url
        headers = {"Authorization": "Bearer {0}".format(self.access_token)}
        headers["Content-Type"] = "application/json"


        # aiohttp session created for post to url to add track to playlist
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url, params=payload) as response:
                print(response.reason)
                response = await response.json()
                
                

    async def playlist_add_items(self, playlist_id, items):
        """ Adds tracks/episodes to a playlist
            Parameters:
                - playlist_id - the id of the playlist
                - items - a list of track/episode URIs, URLs or IDs
        """
        expired = await self.is_expired()
        if expired:
            await self.refresh()
        await self.internal_call(
            "playlists/%s/tracks" % (playlist_id),
            payload=items,
        )
    
    # used to check for each request if token has expired
    async def is_expired(self):
        now = int(time.time())
        return self.expire_time - now < 60

    async def refresh(self):
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
        }
        url = 'https://accounts.spotify.com/api/token'

        id_and_secret = bytes("%s:%s" % (self.client_id, self.client_secret), 'utf-8')

        b64_auth_str = base64.b64encode(id_and_secret).decode('utf-8')

        headers = {'Authorization': 'Basic {0}'.format(b64_auth_str)}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(url, params=payload) as response:
                response = await response.json()
                self.access_token = response['access_token']
                self.expire_time = int(time.time()) + 3600


    
