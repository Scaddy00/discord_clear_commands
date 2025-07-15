# 🧹 Slash Command Cleanup Scripts

These scripts solve the problem of duplicate slash commands in your Discord bot.

## 📋 Problem

If you see duplicate commands like `/role new` twice among slash commands, this is due to:
- Discord cache not updated
- Failed command synchronization
- Commands registered multiple times in the past

## 🛠️ Solutions

### Option 1: Standard Cleanup Script (Recommended)

```bash
python clear_commands.py
```

**What it does:**
- Deletes all existing slash commands
- Resyncs commands from code
- Shows registered commands at the end

### Option 2: Force Cleanup Script (If option 1 doesn't work)

**Before using this script, add to your `.env` file:**
```
APPLICATION_ID=your_application_id
```

**Then run:**
```bash
python force_clear_commands.py
```

**What it does:**
- Uses Discord API to force delete all commands
- Deletes commands one by one via API
- Works even if the bot is offline

## 🔧 Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
# ============================= DISCORD BOT CONFIGURATION =============================

# Discord Bot Token (required)
# Get from: Discord Developer Portal > Applications > Your app > Bot > Token
DISCORD_TOKEN=your_discord_bot_token_here

# Application ID (required for force_clear_commands.py)
# Get from: Discord Developer Portal > Applications > Your app > General Information
APPLICATION_ID=your_application_id_here

# Command Prefix (used by main bot)
COMMAND_PREFIX=!

# Guild ID for DEBUG mode (optional)
# Discord server ID for local testing
GUILD_ID=your_guild_id_here

# Debug Mode (optional)
# 1 = DEBUG mode (commands only for specific guild)
# 0 = PRODUCTION mode (global commands)
DEBUG_MODE=0
```

### 🔧 How to find the values:

**DISCORD_TOKEN:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Go to "Bot" in the sidebar
4. Click "Reset Token" and copy the new token

**APPLICATION_ID:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Go to "General Information"
4. Copy the Application ID

**GUILD_ID:**
1. Enable developer mode in Discord
2. Right-click on server > "Copy ID"

**⚠️ Important:**
- Never share the DISCORD_TOKEN
- Use DEBUG_MODE=1 for local testing
- Use DEBUG_MODE=0 for production

## 📝 Steps to follow

1. **Stop the bot** if it's running
2. **Run the cleanup script** (option 1 or 2)
3. **Restart the bot** with `python main.py`
4. **Verify** that duplicate commands have disappeared

## ⚠️ Important Notes

- **DEBUG Mode**: If `DEBUG_MODE=1` in your `.env`, commands are registered only for the specified guild
- **PRODUCTION Mode**: If `DEBUG_MODE=0`, commands are registered globally
- **Propagation times**: Changes can take up to 1 hour to propagate globally
- **Backup**: Make sure you have a backup of your bot before running the scripts

## 🎯 Expected Result

After running the scripts, you should see:
- ✅ One `/role new` instead of two
- ✅ All commands working correctly
- ✅ No duplicate commands

## 🆘 If the problem persists

If you continue to see duplicates after running the scripts:

1. **Check that there are no multiple bot instances** running
2. **Verify bot settings** in Discord Developer Portal
3. **Wait up to 1 hour** for global propagation
4. **Contact support** if the problem persists

---

**Good luck! 🚀** 