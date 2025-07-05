import logging
import asyncio
from datetime import datetime, time as dtime

from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = "8026623107:AAFFV1v3c7f9XXE6DoxEGiQesB0rNjB4t-k"
CHAT_ID = "@Prashantcdfstbot"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)

async def send_message(text):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="HTML")
    except TelegramError as e:
        logging.error(f"Failed to send message: {e}")

def get_top_business_news():
    return [
        "📈 Sensex closes at record high amid FII inflows.",
        "💼 SEBI approves Tata’s demerger plan.",
        "🚀 PSU banks lead market rally on strong credit growth."
    ]

def get_undervalued_penny_stocks():
    stocks = [
        {"name": "ABC Ltd", "price": 22.5, "book_value": 50, "roe": 12},
        {"name": "XYZ Textiles", "price": 18.3, "book_value": 42, "roe": 9},
    ]
    result = "💎 <b>Undervalued Penny Stocks (Below ₹25)</b>\n"
    for s in stocks:
        result += f"• {s['name']} — Price: ₹{s['price']}, BV: ₹{s['book_value']}, ROE: {s['roe']}%\n"
    return result

def get_corporate_actions():
    return (
        "🔔 <b>Corporate Actions</b>\n"
        "• ABC Ltd announces ₹100 Cr Buyback.\n"
        "• XYZ Textiles approves Demerger of Spinning Unit.\n"
        "• PQR Infra wins SEBI Auction at ₹12/share."
    )

async def morning_update():
    await send_message("🌅 <b>Good Morning! Here are your updates:</b>")
    await send_message(get_undervalued_penny_stocks())
    news = "\n".join([f"• {n}" for n in get_top_business_news()])
    await send_message(f"📰 <b>Top Business News</b>\n{news}")
    await send_message(get_corporate_actions())

async def evening_update():
    await send_message("🌙 <b>Evening Recap:</b>")
    await send_message("📊 Today's gainers/losers below ₹25:\n• DEF +7%\n• GHI -3%")
    await send_message("🤝 Key business deals/orders:\n• LMN Bags ₹500 Cr Railway Order\n• OPQ Signs MoU with NTPC")

async def scheduler():
    while True:
        now = datetime.now().time()
        if now >= dtime(9, 15) and now <= dtime(9, 20):
            await morning_update()
            await asyncio.sleep(300)
        elif now >= dtime(20, 0) and now <= dtime(20, 5):
            await evening_update()
            await asyncio.sleep(300)
        await asyncio.sleep(60)

if __name__ == "__main__":
    logging.info("Bot started.")
    asyncio.run(scheduler())
