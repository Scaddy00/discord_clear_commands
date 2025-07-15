# ----------------------------- Imported Libraries -----------------------------
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

# Load .env file
load_dotenv()

# ============================= GET APPLICATION ID SCRIPT =============================
async def get_application_id():
    """Script per ottenere l'Application ID del bot"""
    
    # Setup bot con intents
    intents = discord.Intents.all()
    intents.messages = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    print("🔄 Connessione al bot per ottenere l'Application ID...")
    
    try:
        # Connessione al bot
        await bot.start(str(getenv('DISCORD_TOKEN')))
    except Exception as e:
        print(f"❌ Errore durante l'avvio del bot: {e}")
        return
    
    try:
        print("⏳ Attendo che il bot sia pronto...")
        await bot.wait_until_ready()
        
        # Ottieni l'Application ID
        application_id = bot.application_id
        print(f"✅ Application ID trovato: {application_id}")
        print(f"📝 Aggiungi questa riga al tuo file .env:")
        print(f"   APPLICATION_ID={application_id}")
        
    except Exception as e:
        print(f"❌ Errore durante il recupero dell'Application ID: {e}")
    
    finally:
        # Chiudi il bot
        await bot.close()
        print("🔚 Bot chiuso")

# ============================= MAIN =============================
if __name__ == "__main__":
    import asyncio
    asyncio.run(get_application_id()) 