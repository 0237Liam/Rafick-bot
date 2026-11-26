# Rafick-bot

Educational Telegram bot for general questions about trading concepts and using the Quotex platform. It replies to users who message the bot, provides brief topic-based educational guidance, and offers optional links to the channel and bot owner's Telegram profile.

> **Risk notice:** This bot does not provide personalized financial advice, trading signals, or guarantees of profit, and it does not place trades. Trading—especially short-term/binary-options-style trading—can result in losing all money committed. Users should check local laws and Quotex's official terms and information for their region.

## Run locally

1. Use Python 3.10 or later.
2. Create a Telegram bot with [@BotFather](https://t.me/BotFather), or retrieve the token for the existing `@crystalloungbot`. Never commit or share the token.
3. Copy `.env.example` to `.env` and set `TELEGRAM_BOT_TOKEN` to the token. Alternatively, export that environment variable directly.
4. Install and start:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   python bot.py
   ```

The bot uses long polling, so keep the process running on a machine or hosting service. Configure `TELEGRAM_BOT_TOKEN` as a secret in your hosting provider rather than putting it in source code. Only one polling instance should run for this bot token at a time.

## Included topics

The starter bot recognizes common questions about demo accounts, risk management, indicators, platform basics, deposits/withdrawals, and scams. It gives a general educational fallback when it doesn't recognize a topic. It does not send unsolicited messages: a user must open the bot and message it first.

Every response includes optional inline buttons for:

- Channel: https://t.me/crytallounge37
- Contact: https://t.me/rafickrathcart37

Update the response text and topic keywords in `bot.py` to customize the educational content. Keep any token out of Git history; if a token is ever exposed, revoke it with BotFather and create a replacement.
