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
    
    print("🔄 Connecting to bot to get Application ID...")
    
    try:
        # Connect to bot
        await bot.start(str(getenv('DISCORD_TOKEN')))
    except Exception as e:
        print(f"❌ Error during bot startup: {e}")
        return
    
    try:
        print("⏳ Waiting for bot to be ready...")
        await bot.wait_until_ready()
        
        # Get Application ID
        application_id = bot.application_id
        print(f"✅ Application ID found: {application_id}")
        print(f"📝 Add this line to your .env file:")
        print(f"   APPLICATION_ID={application_id}")
        
    except Exception as e:
        print(f"❌ Error retrieving Application ID: {e}")
    
    finally:
        # Close bot
        await bot.close()
        print("🔚 Bot closed")

# ============================= MAIN =============================
if __name__ == "__main__":
    import asyncio
    asyncio.run(get_application_id()) 