import logging
from utils.admin_utils import is_bot_admin, is_user_admin

async def moderate_message(bot, message):
    if not message.chat.endswith('@g.us') or message.from_me:
        return
    if await is_user_admin(bot, message.chat, message.sender):
        return
    if await is_bot_admin(bot, message.chat):
        try:
            await bot.delete_message(message)
            logging.info(f"Berhasil menghapus pesan {message.id} dari {message.sender}")
        except Exception as e:
            logging.error(f"Gagal menghapus pesan {message.id}: {e}")
    else:
        logging.warning(f"Bot bukan admin di {message.chat}. Tidak dapat menghapus pesan.")

async def kick_spammer(bot, chat_id: str, spammer_id: str):
    try:
        success = await bot.update_group_participants(
            jid=chat_id,
            action='remove',
            participants=[spammer_id]
        )
        if success:
            user_number = spammer_id.split('@')[0]
            mention_text = (
                f"⚠️ *SPAM TERDETEKSI!*\n\n@{user_number} telah di-kick karena melakukan spam.\n\n"
                f"_Pesan ini adalah tindakan otomatis dari bot anti-spam._"
            )
            await bot.send_mention(chat_id, mention_text, mentions=[spammer_id])
            logging.info(f"Berhasil kick spammer {spammer_id} dari grup {chat_id}")
        else:
            logging.error(f"Gagal kick spammer {spammer_id}")
    except Exception as e:
        logging.error(f"Error saat kick spammer: {e}")