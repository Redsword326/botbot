import discord
import auth
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print("Ready")
    async def on_message(self, message):
        if not message.content.startswith(auth.prefix):
            return
        command = message.content.split(" ")[0].split(auth.prefix)[1]
        args = message.content.split(" ")[1:]

        if command == "roll":
            if len(args) == 1:
                try:
                    if args[0].startswith("d"):
                        roll = random.randint(1, int(args[0].split("d")[1]))
                        await send(message, ":game_die: Rolled " + str(roll), "Rolled a dice")

                    else:
                        dArgs = args[0].split("d")
                        rolls = []
                        x = 0
                        while x < int(dArgs[0]):
                            rolls.append(random.randint(1, int(dArgs[1])))
                            x += 1
                        total = 0
                        dicemsg = ""
                        for x in rolls:
                            total += x
                            dicemsg += ":game_die: `" + str(x) + "`\n"
                
                        await send(message, ":game_die: Rolled " + str(args[0]) + " dice and got: `" + str(total) + "`! \n" + dicemsg, "Rolled " + str(args[0]) + " dice")
                except:
                    await send(message, "Whoops! Your syntax is wrong!", "Tried to roll a dice, but failed. Error: Improper Syntax")
            else:
                await send(message, "Whoops! Too many arguments! It should look like: `!roll d6` or `!roll 2d6`", "Tried to roll a dice, but failed. Error: Too Many Arguments")

        elif command == "fetch":
                if len(args) == 0:
                    try:
                        await send(message, "Börk! Börk!", "Fetched a stick!", responseFile=discord.File("botbotstik.jpg"))
                    except:
                        await send(message, "Whoops! Your syntax is wrong!", "Tried to fetch a stick, but failed. Error: Improper Syntax")
                else:
                    await send(message, "Whoops! Too many arguments! It should look like: '!fetch'", "Tried to fetch a stick, but failed. Error: Too Many Arguments")

        elif command == "coinflip":
                if len(args) == 0:
                    try:
                        flip = random.randint(1, 2)
                        if flip == 1:
                            await send(message, "Heads!", "Flipped a coin!")
                        if flip == 2:
                            await send(message, "Tails!", "Flipped a coin!")
                    except:
                       await send(message, "Whoops! Your syntax is wrong!", "Tried to flip a coin, but failed. Error: Improper Syntax")
                else:
                    await send(message, "Whoops! Too many arguments! It should look like: '!coinflip'", "Tried to flip a coin, but failed. Error: Too Many Arguments")
                    


async def send(message, response, logmsg, responseFile=None, responseEmbed=None):
    await message.channel.send(response, file=responseFile, embed=responseEmbed)
    await client.get_channel(logs channel ID here).send(logmsg)

                

client = MyClient()
client.run(auth.token)