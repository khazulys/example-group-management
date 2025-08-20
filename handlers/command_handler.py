import logging
from pywabot import types
from config.settings import SPAM_THRESHOLD, SPAM_TIMEFRAME
from utils.admin_utils import get_group_admins, is_bot_admin, is_user_admin

async def handle_admin_command(bot, message: types.WaMessage, action: str):
    if not message.quoted:
        await bot.send_message(message.chat, f"Perintah `!{action}` harus reply pesan target.", reply_chat=message)
        return
    admins = await get_group_admins(bot, message.chat)
    if message.sender not in admins:
        await bot.send_message(message.chat, "Hanya admin yang bisa menggunakan perintah ini.", reply_chat=message)
        return
    if not await is_bot_admin(bot, message.chat):
        await bot.send_message(message.chat, "Bot harus jadi admin terlebih dahulu.", reply_chat=message)
        return
    target_jid = message.quoted.sender
    target_number = target_jid.split('@')[0]
    if action in ['remove', 'demote'] and await is_user_admin(bot, message.chat, target_jid):
        await bot.send_message(message.chat, f"Tidak dapat {action} admin grup!", reply_chat=message)
        return
    try:
        success = await bot.update_group_participants(jid=message.chat, action=action, participants=[target_jid])
        if success:
            action_text = {'remove': 'kick', 'promote': 'promosikan', 'demote': 'demote'}.get(action, action)
            response_text = f"✅ Sukses! @{target_number} telah di-{action_text}."
            await bot.send_mention(message.chat, response_text, mentions=[target_jid])
        else:
            await bot.send_message(message.chat, f"❌ Gagal `{action}` @{target_number}.", reply_chat=message)
    except Exception as e:
        logging.error(f"Error '{action}': {e}")
        await bot.send_message(message.chat, f"❌ Terjadi error: {e}", reply_chat=message)

async def spam_info(bot, message: types.WaMessage):
    info_text = (
        f"🤖 *Anti-Spam Bot*\n\n"
        f"⚡ Threshold: {SPAM_THRESHOLD} pesan\n"
        f"⏱️ Timeframe: {SPAM_TIMEFRAME} detik\n"
        f"🔨 Tindakan: Kick otomatis\n\n"
        f"⚠️ Moderasi:\n"
        f"• Gambar/Video (kecuali admin)\n"
        f"• Link (kecuali admin)\n"
        f"• Spam semua pesan\n\n"
        f"🛡️ Admin grup tidak terkena moderasi."
    )
    await bot.send_message(message.chat, info_text, reply_chat=message)

def register_command_handlers(bot):
    @bot.handle_msg('!kick')
    async def kick_member(message: types.WaMessage):
        await handle_admin_command(bot, message, 'remove')

    @bot.handle_msg('!promote')
    async def promote_member(message: types.WaMessage):
        await handle_admin_command(bot, message, 'promote')

    @bot.handle_msg('!demote')
    async def demote_member(message: types.WaMessage):
        await handle_admin_command(bot, message, 'demote')

    @bot.handle_msg('!spam')
    async def show_spam_info(message: types.WaMessage):
        await spam_info(bot, message)