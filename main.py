from telethon import TelegramClient, events
from flask import Flask
import threading

# === НАСТРОЙКИ ===
api_id = 123456      # <-- сюда твой API ID
api_hash = 'abcd1234abcd1234abcd1234abcd1234'  # <-- сюда твой API Hash

# === КЛЮЧЕВЫЕ СЛОВА ДЛЯ ПОИСКА ===
KEYWORDS = [
    'автомобиль на продажу',
    'аеропорт',
    'аэропорт',
    'возьму с собой',
    'куплю авто',
    'куплю машину',
    'куплю пс5',
    'машина в продаже',
    'продается машина',
    'продажа авто',
    'продам playstation',
    'продам авто',
    'продам машину',
    'продам пс5',
    'срочно продам',
    'такси',
    'трансфер',
    # дополнительные варианты
    'авто продажа',
    'машина срочно',
    'продаю авто',
    'продаю машину',
    'ps5 в продаже',
    'playstation 5',
    'куплю ps5',
    'продам ps5',
    'авто б/у',
    'машина б/у',
    'транспорт',
    'такси заказ',
    'трансфер в аэропорт',
    'срочно куплю',
    'куплю транспорт',
    'машину заберу'
]

# === USERBOT ===
client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text.lower()
    for phrase in KEYWORDS:
        if phrase in text:
            chat = await event.get_chat()
            chat_name = getattr(chat, 'title', 'Личные сообщения')
            print(f"\n📌 Найдено в чате: {chat_name}")
            print(f"💬 Сообщение: {event.raw_text}\n")
            break

# === FLASK СЕРВЕР ДЛЯ UPTIMEROBOT ===
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# === ЗАПУСК ===
if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    print("🚀 Userbot запущен. Жду сообщения...")
    client.start()
    client.run_until_disconnected()
