# SpotifyDiscordBot

This discord bot adds tracks to an already existing spotify playlist when a spotify track url is posted in a server. I used the discord.py wrapper for the Discord API (https://github.com/Rapptz/discord.py). I was intending on using the spotipy wrapper for the Spotify API, but learned that discord.py was written using asyncio and was thus asynchronous, while spotipy is not. Not wanting to write blocking code during discord events, this turned out to be a great learning experience in using asyncio/aiohttp for API requests. Sidenote--asyncio & asynchronous programming in general is *hard*. The general syntax, especially for Python, is easy; however the concept was hard for me to wrap my head around at first. I was able to take a seemingly simple side project and pull a lot of new-found knowledge from it. 

If you want to use this for your own bot go ahead and fork this repository. Make sure you are authenticated through the Spotify & Discord APIs. Spotify's API is fairly simple to authenticate with, but Discord's requires a little more thought beforehand depending on scopes you want to allow for your bot. In total you'll need your spotify access token, spotify refresh token, spotify client id & secret, playlist id, and discord token. Once these are set in the environment you should be good to run the bot.py file. 


