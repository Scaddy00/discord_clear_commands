# ----------------------------- Imported Libraries -----------------------------
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
# ----------------------------- Custom Libraries -----------------------------
from bot import WishBot

# Load .env file
load_dotenv()

# ============================= CLEAR COMMANDS SCRIPT =============================
async def clear_all_commands():
    """Script to delete all slash commands and resync from scratch"""
    
    # Setup bot with intents
    intents = discord.Intents.all()
    intents.messages = True
    bot = WishBot(command_prefix=str(getenv('COMMAND_PREFIX')), intents=intents)
    
    print("🔄 Starting command cleanup script...")
    
    try:
        # Connect to bot
        await bot.start(str(getenv('DISCORD_TOKEN')))
    except Exception as e:
        print(f"❌ Error during bot startup: {e}")
        return
    
    try:
        print("⏳ Waiting for bot to be ready...")
        await bot.wait_until_ready()
        
        if getenv("DEBUG_MODE") == "1":
            # DEBUG mode - cleanup commands for specific guild
            dev_guild = discord.Object(id=int(getenv('GUILD_ID')))
            print(f"🧹 Deleting commands for guild: {dev_guild.id}")
            
            # Delete all commands from guild
            bot.tree.clear_commands(guild=dev_guild)
            print("✅ Commands deleted from guild")
            
            # Sync commands with guild
            synced = await bot.tree.sync(guild=dev_guild)
            print(f"✅ Commands resynced with guild: {len(synced)} commands")
            
        else:
            # PRODUCTION mode - cleanup global commands
            print("🌍 Deleting global commands...")
            
            # Delete all global commands
            bot.tree.clear_commands()
            print("✅ Global commands deleted")
            
            # Sync global commands
            synced = await bot.tree.sync()
            print(f"✅ Global commands resynced: {len(synced)} commands")
        
        # Show registered commands
        tree = bot.tree._get_all_commands()
        commands_names = [command.name for command in tree]
        print(f"📋 Currently registered commands: {commands_names}")
        
        print("✅ Cleanup completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
    
    finally:
        # Close bot
        await bot.close()
        print("🔚 Bot closed")

# ============================= MAIN =============================
if __name__ == "__main__":
    import asyncio
    asyncio.run(clear_all_commands()) 