import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

print("Lancement du BOT ...")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("WL Allumée !!!")

    try:
    
        synced = await bot.tree.sync()
        print(f"command wl sync : {len(synced)}")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message: discord.message):
    if message.content.lower() == 'bonjour':
        channel = message.channel
        author = message.author
        await author.send('Salut tu veux passée ta WL !!!')

@bot.tree.command(name="open", description="WL Ouvert")
async def open(interaction: discord.Interaction):
    embed = discord.Embed(
        title="WL OUVERTE",
        description="Les WL sont Ouverte aller dans le vocale Attente WL",
        color=discord.Color.green()
    )
    embed.add_field(name="AstraliaRP WL", value="Rejoin la grande aventure D'astraliaRP WL")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1426162626945089590/1427709993477476534/Astralia_ouvert.png?ex=68f325cc&is=68f1d44c&hm=1c36df738c7c056030e48e8a2aec12b422fb70d63ba0f672a80bbaedb04338ae&")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="close", description="WL Fermer")
async def close(interaction: discord.Interaction):
    embed = discord.Embed(
        title="WL FERMER",
        description="Les WL sont Fermer aller dans le vocale Attente WL",
        color=discord.Color.red()
    )
    embed.add_field(name="AstraliaRP WL", value="Attend la Prochaine Ouverture des WL pour Rejoin la grande aventure D'astraliaRP WL")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1426162626945089590/1427710028139466812/Astralia_ferme.png?ex=68f325d4&is=68f1d454&hm=fea1e2f4e103743518887d854ed4292cab9e15b34663c8fd2ab76856077d08aa&")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="wl", description="Passe ta WL")
async def wl (interaction: discord.Interaction):
    await interaction.response.send_message("Vien dans se channel vocale on vas te moov !!!")

bot.run(os.getenv('DISCORD_TOKEN'))