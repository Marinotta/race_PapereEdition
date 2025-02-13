import discord
from discord.ext import commands
import pandas as pd
import random  # Import the random module
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # This will load the environment variables from .env.txt
token = os.getenv('DISCORD_TOKEN')  # Get the token from the environment

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # Enables access to message content

# Set up the bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Duck GIFs for top performers
duck_gifs = [
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGR3eHpsMGptdXl3dmpqdnRvNmczeTlsaG53c25obTN4cmh2azQyMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7OxMSjThgSRgsHXOFc/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnJ5d2doeW9xc244ZHJndnlzZ3U1dGI4N3l2dHo5MmF0ejBvN3hyZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WYPP1DQ7pnXBUWXdRw/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTltNHFsNmdiaDk4aDk5d2w4aXRqN2I2b2lkN2FzdHVxdXkxOW1kbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2Je24Ke23jHohsvS/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzZ3NWNreXB6cnJrMm5ubjRybnNhdnR4NWgyeHZ6eXNtNDMzYTVsYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RQ7rwyOeftc5z2HTyc/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3RscGpvdXZiaXJ1eXRxNTN2NTFybzF3azQwZmo0Z2JtYnhzbXl1cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/krewXUB6LBja/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW9qNXJvNjNuamg4bTg4cno5bnJqNGdlZ3FudWliZnI0eGZscWp3cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WiTFa9I5AfrEY/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGRvdTRyMzVudWlld2p4dnpudHdkbDdiM3l3cXRseW15OThwaGZvcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/82nxC1u2BC8VU1wiZq/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmIxeWpnN2g4djE2Y2ZvbDVyZWF2cW80ZGpvbzQwaTRoMTQyeGNtdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WUuypTBVGuwhi/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTExa3prc2c0a3U2dnl2OTlpbThuNGUyd2Y0a3kyajV0Nm45aWR4cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YdSSSyGEPkzTi/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXljcWVseXBsa2s2YWRhN2g2bGloZWVtYnoyMTlwcWRpMGc1N2g3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eGph4tozipTDW/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Y1Njg5cjJtczVzNmZtam94ZGNvcThvN2pqZHhxZjE1YzdvZXN0biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/e2CIuhhEz7nJ6/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd25nbnl3eHJzMGE1M2ptem1tbnFnMG41enFqdWNzanloOTRienpwaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wOhhxlCn4e4HaCYQwr/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2ZleXRlbWZtZnJtcHBiaDZvcmNjMmJ0OXBpbzB0cWcweWFuaTR3aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KY5itWvIINKs8/giphy.gif",
    "https://tenor.com/ca/view/duck-sigma-duck-alpha-duck-alpha-male-duck-alpha-female-duck-gif-7005165387130923807"
]

mosconi_gifs = [
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGxjd2h3aDJ2YnVnZTV3eWM0bDFxcmp5enFjazZtZ2twa2pvOHdpYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13QHE6awZWd01G/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDJ2amhnb282ejZjejFxcHFucW16NjFoa2JtbW5xa3dsMTIxYWJ2NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MFCIr88rNNE52/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjBma2o5eXB6ZzQ3MDE3M2tnanpmYzFvY3Z2OGY3dmg2YXExYTc0aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9Oo7oxIVnkN0Zy/giphy.gif"
]

# Command to upload the ranking
@bot.command()
async def rankingPapere(ctx, *, player_name: str = None):
    try:
        # Load the CSV file with explicit delimiter
        df = pd.read_csv('./output100.csv', delimiter=';')
        
        # Clean up player names (strip spaces and normalize)
        df['Nome'] = df['Nome'].str.strip()  # Strip spaces
        df['Nome'] = df['Nome'].apply(lambda x: ' '.join(x.split()))  # Remove extra spaces within names
        
        # Remove rows with NaN values in important columns (e.g., 'Nome' and 'Total Sum')
        df = df.dropna(subset=['Nome', 'Total Sum'])
        
        # Debugging: Print the first few rows and column names
        print(df.head())
        print(df.columns)

        if player_name:
            print(f"Searching for: '{player_name}'")  # Debugging the input
            
            # Make the search case-insensitive and ensure the name matches correctly
            player_data = df[df['Nome'].str.contains(player_name, case=False, na=False)]
            
            if player_data.empty:
                mosconi_gif = random.choice(mosconi_gifs)

                # Create an embed for the Mosconi GIF
                embed = discord.Embed(
                    title="🦆 Player Not Found!",
                    description=f"Player '{player_name}' was not found in the ranking. Try again!",
                    color=discord.Color.red()  # Choose a color for the embed
                )
                embed.set_image(url=mosconi_gif)  # Add the Mosconi GIF as an image

                # Send the embed
                await ctx.send(embed=embed)
                return

            # Get the first matching row
            row = player_data.iloc[0]
            gif = random.choice(duck_gifs)
            # Create an embed with the GIF
            embed = discord.Embed(
                title=f"🦆 Ranking for {row['Nome'].title()} 🦆",
                description=(
                    f"🏅 **Rank**: {row['Rank']}\n"
                    f"📊 **Total Sum**: {row['Total Sum']} points"
                ),
                color=discord.Color.yellow()  # Choose a color for the embed
            )
            embed.set_image(url=gif)  # Add the GIF as an image

            # Send the embed
            await ctx.send(embed=embed)


        else:
            await ctx.send(
                "Here's the full 🦆 **Race Papere Edition** 🦆 ranking:\n"
                "🔗 [Click here to view the ranking](https://lookerstudio.google.com/reporting/8cd9d538-6a88-4fa9-9646-6d786e625a05)"
            )
    except Exception as e:
        mosconi_gif = random.choice(mosconi_gifs)
        await ctx.send(f"❌ Oops! Something went wrong! {mosconi_gif}")
        await ctx.send(f"🛠️ Errore: `{str(e)}`")
        
# Run the bot
bot.run(token)


