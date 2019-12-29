import discord
import auth

class MyClient(discord.Client) {
    async def on_ready(self) {

    }
    async def on_message(self, message) {

    }
}

client = MyClient()
client.run(auth.token);