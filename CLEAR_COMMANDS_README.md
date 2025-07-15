# 🧹 Script di Pulizia Comandi Slash

Questi script risolvono il problema dei comandi slash duplicati nel tuo bot Discord.

## 📋 Problema

Se vedi comandi duplicati come `/role new` due volte tra gli slash command, questo è dovuto a:
- Cache Discord non aggiornata
- Sincronizzazione fallita dei comandi
- Comandi registrati più volte in passato

## 🛠️ Soluzioni

### Opzione 1: Script di Pulizia Standard (Raccomandato)

```bash
python clear_commands.py
```

**Cosa fa:**
- Cancella tutti i comandi slash esistenti
- Risincronizza i comandi dal codice
- Mostra i comandi registrati alla fine

### Opzione 2: Script di Pulizia Forzata (Se l'opzione 1 non funziona)

**Prima di usare questo script, aggiungi al tuo file `.env`:**
```
APPLICATION_ID=il_tuo_application_id
```

**Poi esegui:**
```bash
python force_clear_commands.py
```

**Cosa fa:**
- Usa l'API Discord per forzare la cancellazione di tutti i comandi
- Cancella comandi uno per uno tramite API
- Funziona anche se il bot non è online

## 🔧 Come trovare l'APPLICATION_ID

1. Vai su [Discord Developer Portal](https://discord.com/developers/applications)
2. Seleziona la tua applicazione
3. Vai su "General Information"
4. Copia l'**Application ID**

## 📝 Passi da seguire

1. **Ferma il bot** se è in esecuzione
2. **Esegui lo script di pulizia** (opzione 1 o 2)
3. **Riavvia il bot** con `python main.py`
4. **Verifica** che i comandi duplicati siano scomparsi

## ⚠️ Note Importanti

- **Modalità DEBUG**: Se `DEBUG_MODE=1` nel tuo `.env`, i comandi vengono registrati solo per la guild specificata
- **Modalità PRODUZIONE**: Se `DEBUG_MODE=0`, i comandi vengono registrati globalmente
- **Tempi di propagazione**: I cambiamenti possono richiedere fino a 1 ora per propagarsi globalmente
- **Backup**: Assicurati di avere un backup del tuo bot prima di eseguire gli script

## 🎯 Risultato Atteso

Dopo l'esecuzione degli script, dovresti vedere:
- ✅ Un solo `/role new` invece di due
- ✅ Tutti i comandi funzionanti correttamente
- ✅ Nessun comando duplicato

## 🆘 Se il problema persiste

Se continui a vedere duplicati dopo aver eseguito gli script:

1. **Controlla che non ci siano più istanze del bot** in esecuzione
2. **Verifica le impostazioni del bot** nel Discord Developer Portal
3. **Aspetta fino a 1 ora** per la propagazione globale
4. **Contatta il supporto** se il problema persiste

---

**Buona fortuna! 🚀** 