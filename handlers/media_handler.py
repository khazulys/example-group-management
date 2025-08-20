import re
import logging
from pywabot import types
from utils.admin_utils import is_user_admin
from utils.moderation_utils import moderate_message
from handlers.spam_handler import check_for_spam

async def handle_images(message: types.WaMessage, bot):
    if await check_for_spam(bot, message):
        return
    if not await is_user_admin(bot, message.chat, message.sender):
        logging.info(f"Moderasi gambar dari {message.sender}")
        await moderate_message(bot, message)

async def handle_videos(message: types.WaMessage, bot):
    if await check_for_spam(bot, message):
        return
    if not await is_user_admin(bot, message.chat, message.sender):
        logging.info(f"Moderasi video dari {message.sender}")
        await moderate_message(bot, message)

async def handle_messages(message: types.WaMessage, bot):
    if await check_for_spam(bot, message):
        return
    if message.text and re.search(r'https?://\S+', message.text):
        if not message.text.strip().startswith('!') and not await is_user_admin(bot, message.chat, message.sender):
            logging.info(f"Moderasi link dari {message.sender}")
            await moderate_message(bot, message)

def register_media_handlers(bot):
    @bot.on_image()
    async def moderate_images(message: types.WaMessage):
        await handle_images(message, bot)

    @bot.on_video()
    async def moderate_videos(message: types.WaMessage):
        await handle_videos(message, bot)

    @bot.on_message
    async def moderate_messages(message: types.WaMessage):
        await handle_messages(message, bot)