from aiogram import Bot, Dispatcher, executor, types
import webbrowser
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = token=os.environ.get('TOKEN')

bot = Bot('6597396549:AAEeZZ_5cUoDJ3TMWQJa-EdaylXGx9Ya2To')
dp = Dispatcher(bot)

@dp.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://min.studio')


@dp.message_handler(commands=['start'])

def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to site', url='https://min.studio')
    btn2 = types.InlineKeyboardButton('Work', url='https://min.studio/work')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('About Us', url='https://min.studio/about')
    btn4 = types.InlineKeyboardButton('Contact', url='https://min.studio/contact')
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton('Write Me', url='https://t.me/artoctober')
    markup.row(btn5)
    bot.send_photo(message.chat.id, "https://static.hdrezka.ac/i/2020/11/3/necef6b55b9ebmn98f17z.jpeg")
    bot.send_message(message.chat.id, f'Hello! {message.from_user.username} Welcome to the Minimal_Studio 💙💛' , reply_markup=markup)

@dp.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

@dp.message_handler()
def info (message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello! {message.from_user.username}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
