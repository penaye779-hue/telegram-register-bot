from telegram import Update
from telegram.constants import ChatAction, ParseMode
from telegram.ext import ContextTypes
import asyncio


async def send_card(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    message: str,
    keyboard=None,
    delay=0.8
):
    """
    Premium message sender with typing animation.
    """

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    await asyncio.sleep(delay)

    await update.message.reply_text(
        text=message,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )