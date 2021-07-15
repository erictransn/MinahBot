import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class setClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 0 # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 0, # ID of the role associated with unicode emoji '🔴'.
            discord.PartialEmoji(name='🟡'): 0, # ID of the role associated with unicode emoji '🟡'.
            discord.PartialEmoji(name='green', id=0): 0, # ID of the role associated with a partial emoji's ID.
        }

    async def on_ready(self):
        print(f'{client.user.name} client has connected to Discord!')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to the server'
        )

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id != self.role.message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            return

# set up intents for bot to subsrcibe to events specifically infor from discord guild/server
intents = discord.Intents.default()
intents.members = True

client=setClient(intents=intents)
client.run(TOKEN)