import telebot
from telebot import types
from credential import bot_token
TOKEN = bot_token
bot = telebot.TeleBot(TOKEN)

# Dictionary to track user state
user_states = {}
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
option1 = types.KeyboardButton("✍️ Start to trade")
option2 = types.KeyboardButton("📚 Terms & Rules")
option3 = types.KeyboardButton("🗓 History")
option4 = types.KeyboardButton("❓ Help")
option5 = types.KeyboardButton("🗂️ About NFABOT")
#markup.row(option1)
keyboard.add(option1)
keyboard.add(option2,option3)
keyboard.add(option5,option4)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_states[user_id] = 'start'
    user = message.from_user
    bot.send_message(
        message.chat.id,
        f"""Hello👋,{user.first_name} Welcome to NFABot. 
 
 The purpose of the bot 🤖 is to create a safe trading environment for both the buyer and the seller.Kindly read the Rules and NFA bot guide in the Help section before start trading.""",
            
        reply_markup=keyboard
    )
@bot.message_handler(func=lambda message: True)
def handle_user_response(message):
    if message.text == "🗂️ About NFABOT":
        about = """
          The Future of APEPE and the Now of NFABOT

We're excited to introduce NFABot, a cutting-edge bot with functions similar to top Telegram trading bots, yet featuring unique capabilities that set it apart. We'll share more details soon about its short-term features and how it benefits both NFABot and APEPE.

Current Development/Planning Progress:

- NFABot Telegram Bot (Alpha version - in progress)
- NFABot.com website (in progress)
- $NFABOT Token / Two-way bridge on ETH/BSC (in progress)
- Whitepaper (in progress)

Upcoming Marketing Plans:

When our website and whitepaper are complete, we have the following marketing strategies planned:

- Pre-pinksale sale through the APEPE community for a limited time.
- Ninjapromo Telegram bot to attract users to NFABot and guide them to our pinksale.
- Pinksale to raise liquidity for both ETH and BSC pairs and secure early CEX listings.
- Crypto marketing with our (potentially) new CMO, including influencer posts, YouTube videos, press releases, and a countdown timer on the website for new NFABOT features and custom strategies.
        """
        max_message_length = 4096
        message_parts = [about[i:i + max_message_length] for i in range(0, len(about), max_message_length)]
        for part in message_parts:
            bot.send_message(message.chat.id, part)
    elif message.text =="📚 Terms & Rules":
        about = """
- When you open a trade, the bot creates a spot position with a token on Ethereum or Binance Smart Chain.
- NFABot offers all modern trading bot features and continuous improvements.
- Minimum buy-in is 0.01 ETH or 0.05 BNB.
- Users can choose to buy NFABOT, APEPE, or a combination for discounts or fee exemptions.
- The bot only taxes users on profits with varying tax rates based on profit percentages.
- To incentivize holding, we'll determine required amounts of NFABOT and/or APEPE every three months.
- NFABOT holders receive reflections with limits.
- Users can opt to buy and burn partner tokens with the sell tax from the NFABOT token.
- 9 percent sell tax on the NFABOT token, divided into reflections, buying and burning chosen tokens, and treasury/LP injections/charity. No buy tax.
        """
        max_message_length = 4096
        message_parts = [about[i:i + max_message_length] for i in range(0, len(about), max_message_length)]
        for part in message_parts:
            bot.send_message(message.chat.id, part)
    elif message.text == "❓ Help":
        keyboard = types.InlineKeyboardMarkup()
        settings = types.InlineKeyboardButton("How to use NFAbot⚙️", callback_data="how")
        support = types.InlineKeyboardButton("support📞☎️", callback_data="support")
        question = types.InlineKeyboardButton("FAQ⁉️❗", callback_data="support")
        keyboard.add(settings)
        keyboard.add(support,question)
        response = 'Browse help categories'
        bot.send_message(message.chat.id, response,reply_markup=keyboard)
    elif message.text == "✍️ Start to trade":
        keyboard = types.InlineKeyboardMarkup()
        accept = types.InlineKeyboardButton('Accept✅', callback_data="accept")
        Decline = types.InlineKeyboardButton('Decline❌', callback_data='decline')
        keyboard.add(accept,Decline)
        text = 'To continue NFABOT, read nfa news and validate that you accept the Terms & rules (https://nfanews.com/ ) of NFABot.'
        bot.send_message(message.chat.id, text,reply_markup=keyboard)
    else:
        text = 'Sorry i don\'t understand the command'
        bot.send_message(message.chat.id, text)
            
        
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_button_callback(call):
    if call.data == "how":
        bot.send_message(call.message.chat.id, "Here are instructions on how to use NFAbot.")
    elif call.data == "support":
        # Handle the "support📞☎️" button
        bot.send_message(call.message.chat.id, "If you need support, contact us at support@example.com.")
    elif call.data == "faq":
        # Handle the "FAQ⁉️❗" button
        bot.send_message(call.message.chat.id, "Frequently Asked Questions (FAQ) can be found on our website.")
    elif call.data == "accept":
        text ="Are you a buyer or seller?"
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buyer = types.KeyboardButton("I am buyer💸")
        seller = types.KeyboardButton("I am seller🧑🏻‍💻")
        back = types.KeyboardButton("⬅️Back")
        keyboard.add(buyer, seller)
        keyboard.add(back)
        bot.send_message(call.message.chat.id, text,reply_markup=keyboard)
    elif call.data == "decline":
        text = 'The process has been cancelled!'
        bot.send_message(call.message.chat.id, text)
    



           
if __name__ == "__main__":
    bot.polling(none_stop=True)
    