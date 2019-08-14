# telebot-notes
import telebot;
from telebot import types
bot = telebot.TeleBot('');
time = ''
data = ''
note = ''
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты запустил бот')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Напишите "Добавить", что бы добавить событие')
@bot.message_handler(content_types=['text'])
def timer(message):
  if message.text.lower() == 'добавить':
        bot.send_message(message.from_user.id, " Введите время");
        bot.register_next_step_handler(message, get_time);
  else:
       bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
def get_time(message):
        global time;
        time = message.text
        bot.send_message(message.from_user.id, 'Теперь дату');
        bot.register_next_step_handler(message, get_data);
def get_data(message):
        global data;
        data = message.text
        bot.send_message(message.from_user.id, 'Что вам сообщить?');
        bot.register_next_step_handler(message, get_note);
def get_note(message):
       global note
       note = message.text
       keyboard = types.InlineKeyboardMarkup();
       key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
       keyboard.add(key_yes);
       key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
       keyboard.add(key_no);
       question = 'Время-'+time+' Дата-'+data+' Напоминание-'+note+'. Верно?';
       bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )');
    else:
        timer()
bot.polling(none_stop=True, interval=0)
