# ----------------------------- Imported Libraries -----------------------------
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

# Load .env file
load_dotenv()

# ============================= GET APPLICATION ID SCRIPT =============================
async def get_application_id():
    """Script to get the bot's Application ID"""
    
    # Setup bot with intents
    intents = discord.Intents.all()
    intents.messages = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    # Flag to track when we've got the application ID
    application_id_received = False
    
    @bot.event
    async def on_ready():
        """Event triggered when bot is ready"""
        nonlocal application_id_received
        print(f"✅ Bot is ready! Logged in as {bot.user}")
        
        # Get Application ID
        application_id = bot.application_id
        print(f"✅ Application ID found: {application_id}")
        print(f"📝 Add this line to your .env file:")
        print(f"   APPLICATION_ID={application_id}")
        
        application_id_received = True
        
        # Close the bot after getting the ID
        await bot.close()
    
    print("🔄 Connecting to bot to get Application ID...")
    
    try:
        # Connect to bot
        await bot.start(str(getenv('DISCORD_TOKEN')))
    except Exception as e:
        print(f"❌ Error during bot startup: {e}")
        return
    
    if application_id_received:
        print("🔚 Bot closed successfully")
    else:
        print("❌ Failed to get Application ID")

# ============================= MAIN =============================
if __name__ == "__main__":
    import asyncio
    asyncio.run(get_application_id()) 