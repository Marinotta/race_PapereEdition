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
    
]

mosconi_gifs = [
    "https://tenor.com/ca/view/if-i-don-curse-italian-meme-gif-12268541",
    "https://tenor.com/ca/view/germano-mosconi-gif-14446759386453302977",
    "https://tenor.com/ca/view/germano-mosconi-gif-20862777",
    "https://tenor.com/ca/view/bestemmia-gif-7543959",
    "https://tenor.com/ca/view/if-i-dont-curse-now-italian-meme-gif-12268654",
    "https://tenor.com/ca/view/mosconi-pugno-gif-24424526",
    "https://tenor.com/ca/view/germano-mosconi-germanomosconi-mona-porta-gif-8567467",
    "https://tenor.com/ca/view/portanna-mosconi-portannalamadonna-gif-11830913"
]

# Command to upload the ranking
@bot.command()
async def rankingPapere(ctx, player_name: str = None):
    try:
        # Load the CSV
        df = pd.read_csv(r'./output100.csv', delimiter=",")
        
        if player_name:
            # Search for the player in the CSV
            player_data = df[df['Nome'].str.contains(player_name, case=False, na=False)]
            
            if player_data.empty:
                await ctx.send(f"Player '{player_name}' not found in the ranking!")
                return
            
            # Send the specific player's ranking
            ranking_message = f"🦆 **{player_name}'s Ranking** 🦆\n\n"
            for index, row in player_data.iterrows():
                gif = random.choice(duck_gifs)  # Select a random GIF
                ranking_message += f"{index + 1}. {row['Nome']} - {row['Total Sum']} points\n"
                ranking_message += f"{gif}\n"  # Add the GIF to the message
            
            await ctx.send(ranking_message)
        else:
            # If no player name is provided, show the Looker Studio link
            await ctx.send(
                "Here's the full 🦆 **Race Papere Edition** 🦆 ranking:\n"
                "🔗 [Click here to view the ranking] (https://lookerstudio.google.com/reporting/8cd9d538-6a88-4fa9-9646-6d786e625a05)"
            )
    except Exception as e:
        # When an error occurs, show the "Oops!" message with a random Mosconi GIF
        mosconi_gif = random.choice(mosconi_gifs)
        await ctx.send(f"Oops! Something went wrong! {mosconi_gif}")
        print(e)

# Run the bot
bot.run(token)