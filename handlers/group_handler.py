import logging
from typing import List
from config.settings import SPAM_THRESHOLD, SPAM_TIMEFRAME

bot_lid=[]
async def handle_group_update(bot, jid: str, action: str, participants: List[str]):
    if action == 'add':
        try:
            group_meta = await bot.get_group_metadata(jid)
            group_name = group_meta.get('subject', 'Grup Ini')
            participant_names = {p['id']: p.get('notify') or p.get('name') for p in group_meta.get('participants', [])}
            for participant_jid in participants:
                user_number = participant_jid.split('@')[0]
                user_name = participant_names.get(participant_jid, user_number)
                welcome_message = (
                    f"🎉 Selamat bergabung di {group_name}!\n\n"
                    f"Halo @{user_number}, semoga betah di sini!\n\n"
                    f"⚠️ Bot anti-spam aktif. Lebih dari {SPAM_THRESHOLD} pesan "
                    f"dalam {SPAM_TIMEFRAME} detik = kick otomatis.\n\n"
                    f"Patuhilah rules grup."
                )
                await bot.send_mention(jid=jid, text=welcome_message, mentions=[participant_jid])
                logging.info(f"Pesan welcome terkirim ke {user_name} di '{group_name}'")
        except Exception as e:
            logging.error(f"Gagal proses anggota baru: {e}")
    
    if action == 'promote':
        try:
            group_meta = await bot.get_group_metadata(jid)
            group_name = group_meta.get('subject', 'Grup Ini')
            participant_names = {p['id']: p.get('notify') or p.get('name') for p in group_meta.get('participants', [])}
            
            print(participant_names)
        except Exception:
            pass
def register_group_handlers(bot):
    @bot.on_group_participants_update
    async def group_update_handler(jid: str, action: str, participants: List[str]):
        await handle_group_update(bot, jid, action, participants)