import logging

async def get_group_admins(bot, jid: str) -> list:
    try:
        meta = await bot.get_group_metadata(jid)
        participants = meta.get('participants', [])
        return [p['id'] for p in participants if p.get('admin') in ['admin', 'superadmin']]
    except Exception as e:
        logging.error(f"Gagal mendapatkan metadata grup untuk {jid}: {e}")
        return []

async def is_bot_admin(bot, jid: str) -> bool:
    try:
        return await bot.is_bot_admin(jid)
    except Exception as e:
        logging.error(f"Error saat memeriksa status admin bot: {e}")
        return False

async def is_user_admin(bot, chat_id: str, user_id: str) -> bool:
    try:
        admins = await get_group_admins(bot, chat_id)
        print(admins)
        
        return user_id in admins
    except Exception as e:
        logging.error(f"Error saat memeriksa status admin user: {e}")
        return False