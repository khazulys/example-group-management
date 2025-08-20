import time
import logging
from collections import defaultdict
from pywabot import types
from config.settings import SPAM_THRESHOLD, SPAM_TIMEFRAME
from utils.admin_utils import is_bot_admin
from utils.moderation_utils import kick_spammer

user_message_timestamps = defaultdict(lambda: defaultdict(list))

async def check_for_spam(bot, message: types.WaMessage) -> bool:
    if message.from_me or not message.chat.endswith('@g.us'):
        return False
    current_time = time.time()
    chat_id = message.chat
    sender_id = message.sender
    timestamps = user_message_timestamps[chat_id][sender_id]
    user_message_timestamps[chat_id][sender_id] = [t for t in timestamps if current_time - t < SPAM_TIMEFRAME]
    user_message_timestamps[chat_id][sender_id].append(current_time)
    logging.debug(f"Pesan dari {sender_id}. Jumlah pesan: {len(user_message_timestamps[chat_id][sender_id])}/{SPAM_THRESHOLD}")
    if len(user_message_timestamps[chat_id][sender_id]) > SPAM_THRESHOLD:
        logging.warning(f"Spam terdeteksi: {sender_id} di grup {chat_id}")
        user_message_timestamps[chat_id][sender_id] = []
        if await is_bot_admin(bot, chat_id):
            try:
                await kick_spammer(bot, chat_id, sender_id)
                return True
            except Exception as e:
                logging.error(f"Gagal menangani spam: {e}")
        else:
            logging.warning(f"Bot bukan admin di {chat_id}, tidak dapat menangani spam.")
        return True
    return False

def register_spam_handlers(bot):
    pass