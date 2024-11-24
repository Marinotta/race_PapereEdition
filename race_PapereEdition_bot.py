import discord
from discord.ext import commands
import pandas as pd
import random  # Import the random module
import os
from dotenv import load_dotenv

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
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGJjNzZmeGFtamN3NTBjbm9iOHMxd2diZ3IyNGI1bjRvY2lnZzA2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7OxMSjThgSRgsHXOFc/giphy.gif"
]

# Command to upload the ranking
@bot.command()
# Command to upload the ranking
@bot.command()
async def rankingPapere(ctx, player_name: str = None):
    try:
        # Load the CSV
        df = pd.read_csv(r'./output100.csv')
        
        if player_name:
            # Search for the player in the CSV
            player_data = df[df['Player'].str.contains(player_name, case=False, na=False)]
            
            if player_data.empty:
                await ctx.send(f"Player '{player_name}' not found in the ranking!")
                return
            
            # Send the specific player's ranking
            ranking_message = f"🦆 **{player_name}'s Ranking** 🦆\n\n"
            for index, row in player_data.iterrows():
                gif = random.choice(duck_gifs)  # Select a random GIF
                ranking_message += f"{index + 1}. {row['Player']} - {row['Total Sum']} points\n"
                ranking_message += f"{gif}\n"  # Add the GIF to the message
            
            await ctx.send(ranking_message)
        else:
            # If no player name is provided, show the full ranking
            ranking_message = "🦆 **Race Papere Edition** 🦆\n\n"
            for index, row in df.iterrows():
                gif = random.choice(duck_gifs)  # Select a random GIF
                ranking_message += f"{index + 1}. {row['Player']} - {row['Total Sum']} points\n"
                ranking_message += f"{gif}\n"  # Add the GIF to the message

            # Send the full ranking message
            await ctx.send(ranking_message)
            
    except Exception as e:
        await ctx.send("Oops! Something went wrong!")
        print(e)

# Run the bot
bot.run(token)  # Use the token securely