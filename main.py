import discord
import auth

class MyClient(discord.Client):
    async def on_ready(self):
        console.log(message)
    async def on_message(self, message):
        console.log(message)

client = MyClient()
client.run(auth.token)