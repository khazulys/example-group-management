from .spam_handler import register_spam_handlers
from .media_handler import register_media_handlers
from .command_handler import register_command_handlers
from .group_handler import register_group_handlers

def register_handlers(bot):
    register_spam_handlers(bot)
    register_media_handlers(bot)
    register_command_handlers(bot)
    register_group_handlers(bot)