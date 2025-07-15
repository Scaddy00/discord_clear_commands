# ----------------------------- Imported Libraries -----------------------------
import aiohttp
import asyncio
from dotenv import load_dotenv
from os import getenv

# Load .env file
load_dotenv()

# ============================= FORCE CLEAR COMMANDS SCRIPT =============================
async def force_clear_commands():
    """Script per forzare la cancellazione di tutti i comandi slash tramite API Discord"""
    
    TOKEN = getenv('DISCORD_TOKEN')
    APPLICATION_ID = getenv('APPLICATION_ID')  # Aggiungi questa variabile al tuo .env
    GUILD_ID = getenv('GUILD_ID')
    DEBUG_MODE = getenv("DEBUG_MODE") == "1"
    
    if not APPLICATION_ID:
        print("❌ ERRORE: Devi aggiungere APPLICATION_ID al tuo file .env")
        print("   Puoi trovarlo nel Discord Developer Portal > Applications > La tua app > General Information")
        return
    
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    
    base_url = f"https://discord.com/api/v10/applications/{APPLICATION_ID}"
    
    print("🔄 Avvio script di pulizia forzata comandi...")
    
    async with aiohttp.ClientSession() as session:
        try:
            if DEBUG_MODE and GUILD_ID:
                # Modalità DEBUG - cancella comandi dalla guild
                print(f"🧹 Cancellazione forzata comandi per guild: {GUILD_ID}")
                
                # Ottieni tutti i comandi della guild
                async with session.get(f"{base_url}/guilds/{GUILD_ID}/commands", headers=headers) as resp:
                    if resp.status == 200:
                        commands = await resp.json()
                        print(f"📋 Trovati {len(commands)} comandi nella guild")
                        
                        # Cancella ogni comando
                        for command in commands:
                            command_id = command['id']
                            command_name = command['name']
                            
                            async with session.delete(f"{base_url}/guilds/{GUILD_ID}/commands/{command_id}", headers=headers) as del_resp:
                                if del_resp.status == 204:
                                    print(f"✅ Cancellato comando: {command_name}")
                                else:
                                    print(f"❌ Errore nel cancellare comando {command_name}: {del_resp.status}")
                    else:
                        print(f"❌ Errore nel recuperare comandi: {resp.status}")
                
                print("✅ Pulizia comandi guild completata!")
                
            else:
                # Modalità PRODUZIONE - cancella comandi globali
                print("🌍 Cancellazione forzata comandi globali...")
                
                # Ottieni tutti i comandi globali
                async with session.get(f"{base_url}/commands", headers=headers) as resp:
                    if resp.status == 200:
                        commands = await resp.json()
                        print(f"📋 Trovati {len(commands)} comandi globali")
                        
                        # Cancella ogni comando
                        for command in commands:
                            command_id = command['id']
                            command_name = command['name']
                            
                            async with session.delete(f"{base_url}/commands/{command_id}", headers=headers) as del_resp:
                                if del_resp.status == 204:
                                    print(f"✅ Cancellato comando: {command_name}")
                                else:
                                    print(f"❌ Errore nel cancellare comando {command_name}: {del_resp.status}")
                    else:
                        print(f"❌ Errore nel recuperare comandi: {resp.status}")
                
                print("✅ Pulizia comandi globali completata!")
            
            print("\n🎉 Pulizia forzata completata!")
            print("💡 Ora riavvia il bot con 'python main.py' per registrare i comandi puliti")
            
        except Exception as e:
            print(f"❌ Errore durante la pulizia: {e}")

# ============================= MAIN =============================
if __name__ == "__main__":
    asyncio.run(force_clear_commands()) 