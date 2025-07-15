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
    """Script per cancellare tutti i comandi slash e risincronizzare da zero"""
    
    # Setup bot con intents
    intents = discord.Intents.all()
    intents.messages = True
    bot = WishBot(command_prefix=str(getenv('COMMAND_PREFIX')), intents=intents)
    
    print("🔄 Avvio script di pulizia comandi...")
    
    try:
        # Connessione al bot
        await bot.start(str(getenv('DISCORD_TOKEN')))
    except Exception as e:
        print(f"❌ Errore durante l'avvio del bot: {e}")
        return
    
    try:
        print("⏳ Attendo che il bot sia pronto...")
        await bot.wait_until_ready()
        
        if getenv("DEBUG_MODE") == "1":
            # Modalità DEBUG - pulizia comandi per guild specifica
            dev_guild = discord.Object(id=int(getenv('GUILD_ID')))
            print(f"🧹 Cancellazione comandi per guild: {dev_guild.id}")
            
            # Cancella tutti i comandi dalla guild
            bot.tree.clear_commands(guild=dev_guild)
            print("✅ Comandi cancellati dalla guild")
            
            # Sincronizza i comandi con la guild
            synced = await bot.tree.sync(guild=dev_guild)
            print(f"✅ Comandi risincronizzati con la guild: {len(synced)} comandi")
            
        else:
            # Modalità PRODUZIONE - pulizia comandi globali
            print("🌍 Cancellazione comandi globali...")
            
            # Cancella tutti i comandi globali
            bot.tree.clear_commands()
            print("✅ Comandi globali cancellati")
            
            # Sincronizza i comandi globali
            synced = await bot.tree.sync()
            print(f"✅ Comandi globali risincronizzati: {len(synced)} comandi")
        
        # Mostra i comandi registrati
        tree = bot.tree._get_all_commands()
        commands_names = [command.name for command in tree]
        print(f"📋 Comandi attualmente registrati: {commands_names}")
        
        print("✅ Pulizia completata con successo!")
        
    except Exception as e:
        print(f"❌ Errore durante la pulizia: {e}")
    
    finally:
        # Chiudi il bot
        await bot.close()
        print("🔚 Bot chiuso")

# ============================= MAIN =============================
if __name__ == "__main__":
    import asyncio
    asyncio.run(clear_all_commands()) 