import logging
import os
import re
from typing import Final

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

CHANNEL_URL: Final = "https://t.me/crytallounge37"
OWNER_URL: Final = "https://t.me/rafickrathcart37"

DISCLAIMER: Final = (
    "Educational information only—not personalized financial advice or a trading signal. "
    "Trading can result in losing money; there are no guaranteed profits."
)

TOPICS: Final = [
    (
        re.compile(r"\b(demo|practice|virtual balance|demo account)\b", re.I),
        "A demo account is a way to explore platform features with virtual funds. "
        "Results in a demo environment may differ from live trading, and practice does not remove financial risk. "
        "Check Quotex's official help and terms for the features available in your region.",
    ),
    (
        re.compile(r"\b(risk|manage|management|loss|lose|losing|budget|afford)\b", re.I),
        "Risk management means thinking about potential losses before making a decision. "
        "Never trade with borrowed money or money needed for essentials, and consider setting personal limits "
        "or stopping if trading is causing stress. No risk-control method can guarantee a profit or prevent losses.",
    ),
    (
        re.compile(r"\b(indicator|indicators|rsi|macd|moving average|chart|technical analysis)\b", re.I),
        "Technical indicators summarize past price data; they do not predict the future with certainty. "
        "Learn what an indicator measures, its limitations, and how it can behave in different market conditions. "
        "Avoid treating any indicator or combination as a guaranteed entry signal.",
    ),
    (
        re.compile(r"\b(quotex|platform|account|how does it work|binary options?)\b", re.I),
        "For platform features, account requirements, fees, and product terms, use Quotex's official website "
        "and help materials for your location. Product availability and applicable rules can vary by region. "
        "Make sure you understand how a product works and its potential loss before using it.",
    ),
    (
        re.compile(r"\b(deposit|withdraw|withdrawal|payment|payout)\b", re.I),
        "For deposits or withdrawals, check the platform's official instructions, processing times, and terms "
        "for your region. Never send account passwords, verification codes, or payment details to someone in chat; "
        "contact platform support through official channels if something seems wrong.",
    ),
    (
        re.compile(r"\b(scam|fraud|guarantee|guaranteed|signal|signals|profit|profits)\b", re.I),
        "Be cautious of anyone promising guaranteed returns, asking for your password or verification code, "
        "or pressuring you to deposit money. Trading signals are not guarantees. Verify claims independently, "
        "use official support channels, and never share account credentials.",
    ),
]

KEYBOARD: Final = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join the channel", url=CHANNEL_URL)],
        [InlineKeyboardButton("Contact @rafickrathcart37", url=OWNER_URL)],
    ]
)

WELCOME: Final = (
    "Hi! I can share general educational information about trading concepts and the Quotex platform. "
    "Ask about demo accounts, risk, indicators, platform basics, or deposits and withdrawals.\n\n"
    f"{DISCLAIMER}"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    del context
    if update.message:
        await update.message.reply_text(WELCOME, reply_markup=KEYBOARD)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    del context
    if update.message:
        await update.message.reply_text(
            "Send a question about a trading concept or the Quotex platform. Try: "
            "'What is a demo account?', 'How do indicators work?', or 'How can I recognize a scam?'\n\n"
            f"{DISCLAIMER}",
            reply_markup=KEYBOARD,
        )


async def answer_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    del context
    if not update.message or not update.message.text:
        return

    text = update.message.text
    answer = next((response for pattern, response in TOPICS if pattern.search(text)), None)
    if answer is None:
        answer = (
            "I can provide general educational information, but I may not recognize that topic yet. "
            "Try asking about demo accounts, risk management, indicators, platform basics, "
            "deposits/withdrawals, or how to spot scams. For account-specific help, use Quotex's official support."
        )

    await update.message.reply_text(
        f"{answer}\n\n{DISCLAIMER}",
        reply_markup=KEYBOARD,
    )


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("Set the TELEGRAM_BOT_TOKEN environment variable before starting the bot.")

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer_message))
    logger.info("Starting educational Telegram bot polling")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
