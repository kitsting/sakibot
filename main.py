import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


load_dotenv()


@client.event
async def on_ready():
    await tree.sync()
    print("I'm the real Asamiya Saki")


@tree.command(name="clip", description="Get a clip from the show")
async def clip(interaction: discord.Interaction, clip_name: str = ""):
    clip_name = (clip_name.lower()
                 .replace("_","")
                 .replace(" ","")
                 .replace("-","")
                 .replace("'",""))

    if clip_name != "": #Get specific clip
        if os.path.isfile("clips/"+clip_name+".mp4"):
            await interaction.response.send_message("Clip - "+clip_name, file=discord.File("clips/"+clip_name+".mp4"))
        else:
            await interaction.response.send_message(clip_name + " isn't a valid clip", ephemeral=True)
    else: #Get random clip
        filenames = os.listdir("clips")
        if len(filenames) > 0:
            use_clip = random.choice(filenames)
            await interaction.response.send_message("Clip - "+use_clip.replace(".mp4",""), file=discord.File("clips/"+use_clip))
        else:
            await interaction.response.send_message("The clips folder is empty", ephemeral=True)





@tree.command(name="real_saki", description="Test command")
async def real_saki(interaction: discord.Interaction):
    await interaction.response.send_message("I'm the real Asamiya Saki")


client.run(os.getenv("TOKEN"))