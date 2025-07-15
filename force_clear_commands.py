# ----------------------------- Imported Libraries -----------------------------
import aiohttp
import asyncio
from dotenv import load_dotenv
from os import getenv

# Load .env file
load_dotenv()

# ============================= FORCE CLEAR COMMANDS SCRIPT =============================
async def force_clear_commands():
    """Script to force delete all slash commands via Discord API"""
    
    TOKEN = getenv('DISCORD_TOKEN')
    APPLICATION_ID = getenv('APPLICATION_ID')  # Add this variable to your .env
    GUILD_ID = getenv('GUILD_ID')
    DEBUG_MODE = getenv("DEBUG_MODE") == "1"
    
    if not APPLICATION_ID:
        print("❌ ERROR: You need to add APPLICATION_ID to your .env file")
        print("   You can find it in Discord Developer Portal > Applications > Your app > General Information")
        return
    
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    
    base_url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}"
    
    print("🔄 Starting forced command cleanup script...")
    
    async with aiohttp.ClientSession() as session:
        try:
            if DEBUG_MODE and GUILD_ID:
                # DEBUG mode - delete commands from guild
                print(f"🧹 Forced deletion of commands for guild: {GUILD_ID}")
                
                # Get all guild commands
                async with session.get(f"{base_url}/guilds/{GUILD_ID}/commands", headers=headers) as resp:
                    if resp.status == 200:
                        commands = await resp.json()
                        print(f"📋 Found {len(commands)} commands in guild")
                        
                        # Delete each command
                        for command in commands:
                            command_id = command['id']
                            command_name = command['name']
                            
                            async with session.delete(f"{base_url}/guilds/{GUILD_ID}/commands/{command_id}", headers=headers) as del_resp:
                                if del_resp.status == 204:
                                    print(f"✅ Deleted command: {command_name}")
                                else:
                                    print(f"❌ Error deleting command {command_name}: {del_resp.status}")
                    else:
                        print(f"❌ Error retrieving commands: {resp.status}")
                
                print("✅ Guild command cleanup completed!")
                
            else:
                # PRODUCTION mode - delete global commands
                print("🌍 Forced deletion of global commands...")
                
                # Get all global commands
                async with session.get(f"{base_url}/commands", headers=headers) as resp:
                    if resp.status == 200:
                        commands = await resp.json()
                        print(f"📋 Found {len(commands)} global commands")
                        
                        # Delete each command
                        for command in commands:
                            command_id = command['id']
                            command_name = command['name']
                            
                            async with session.delete(f"{base_url}/commands/{command_id}", headers=headers) as del_resp:
                                if del_resp.status == 204:
                                    print(f"✅ Deleted command: {command_name}")
                                else:
                                    print(f"❌ Error deleting command {command_name}: {del_resp.status}")
                    else:
                        print(f"❌ Error retrieving commands: {resp.status}")
                
                print("✅ Global command cleanup completed!")
            
            print("\n🎉 Forced cleanup completed!")
            print("💡 Now restart the bot with 'python main.py' to register clean commands")
            
        except Exception as e:
            print(f"❌ Error during cleanup: {e}")

# ============================= MAIN =============================
if __name__ == "__main__":
    asyncio.run(force_clear_commands()) 