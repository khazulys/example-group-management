import asyncio
import logging
from pywabot import PyWaBot
from pywabot.logging import setup_logging
from config.settings import APIKEY, SESSION
from handlers import register_handlers

setup_logging('info')
bot = PyWaBot(session_name=SESSION, api_key=APIKEY)

async def main():
    try:
        if not await bot.connect():
            phone_number = int(input("Enter your phone number (e.g., 628): "))
            code = await bot.request_pairing_code(phone_number)
            if code:
                print(f"Your pairing code: {code}")
                print("Waiting for connection after pairing...")
                if await bot.wait_for_connection(timeout=120):
                    print("Bot connected successfully!")
                    register_handlers(bot)
                    await bot.start_listening()
                else:
                    print("Connection timeout after pairing.")
            else:
                print("Failed to request pairing code.")
                
        else:
            print("bot ready to incomming message!")
            register_handlers(bot)
            await bot.start_listening()
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    
if __name__ == "__main__":
    asyncio.run(main())
