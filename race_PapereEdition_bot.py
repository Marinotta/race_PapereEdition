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
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGMwMTZnbndkNmw3ODFndjkxa2c3amNkamMybWRkOWI2ZDllZGV0NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RQ7rwyOeftc5z2HTyc/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTBpMzVpaWlseWdmYmt5c3RpZDJ4YnU4ZzhmY29qcWdqZGU0NG5kZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2Je1eIySBj8c94ly/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Fjb2R5MWlkdjl0YWEzdXZsbHZ2amVhdndhN2xwanNrYjk5a3lxMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6MbaZ4f6650Xv3kA/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExajZmczFqcXNjbm0xZXpkMDZjMDU1d2Zvd3AxeG0yYnNqMXlyZWc5NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6MbkfI3ERA6yTqPm/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTJpOGM3NDh1Zzg5dXBpd2tjaHpjZmN0ZWphMmpvNGt3cGg5MnI4biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUOwG3MyaiItznFs6k/giphy-downsized-large.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2RkczQ2OHlrdTBtZWN0cHQzOWh5eWtnOGpmejhxbmp3eTEzdDduaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WYPP1DQ7pnXBUWXdRw/giphy-downsized-large.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGJjNzZmeGFtamN3NTBjbm9iOHMxd2diZ3IyNGI1bjRvY2lnZzA2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7OxMSjThgSRgsHXOFc/giphy.gif",
    "https://tenor.com/ca/view/shenmue-shenmue2-shenmue-duck-racing-shenmue-duck-racing-start-duck-racing-gif-25744150",
    "https://tenor.com/ca/view/excited-dancing-ducks-gif-3639054",
    "https://tenor.com/ca/view/running-ducks-ducks-running-racing-racing-ducks-gif-27273716",
    "https://tenor.com/ca/view/vlod-rubber-duck-duck-vlod2-bathtub-gif-3004830228421712541",
    "https://i.gifer.com/XOsX.gif",
    "https://tenor.com/ca/view/ducks-ducks-are-laughing-laughter-point-a-finger-ducks-laughing-gif-12948112141241137122",
    "https://tenor.com/ca/view/duck-sigma-duck-alpha-duck-alpha-male-duck-alpha-female-duck-gif-7005165387130923807",
    "https://tenor.com/ca/view/duck-waddle-gif-12573743802001671415"
]

mosconi_gifs = [
    "https://tenor.com/view/mosconi-germano-mosconi-ah-non-lo-so-io-gif-11967977",
    "https://tenor.com/view/mosconi-germano-chop-chop-chiss%C3%A0che-non-m-incazza-eh-gif-14096850",
    "https://tenor.com/ca/view/if-i-dont-curse-now-italian-meme-gif-12268654",
    "https://tenor.com/ca/view/non-bestemmiare-germano-mosconi-gif-24841842",
    "https://tenor.com/ca/view/germano-mosconi-non%C3%A8possibile-dio-cane-gif-21765301",
    "https://tenor.com/ca/view/germano-mosconi-vai-in-mona-porco-dio-gif-16047543",
    "https://tenor.com/ca/view/mosconi-ma-che-oh-gif-12572262",
    "https://tenor.com/ca/view/if-i-don-curse-italian-meme-gif-12268541",
    "https://tenor.com/ca/view/portanna-mosconi-portannalamadonna-gif-11830913"
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


