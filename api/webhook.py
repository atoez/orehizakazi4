import json
import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 🔐 ВСТАВЬ СЮДА НОВЫЙ ТОКЕН
        TOKEN = 'f9LHodD0cOLOZI8Ch2Q7MszISpH1nlj_MHzijGbHpu0cJULDfQhezUL6_33YwQheq3AmcOOSWfqiABnK2ew5'
        WEB_APP_URL = 'https://atoez.github.io/orehizakazi/'
        API_URL = 'https://api.max.ru/bot'
        
        # Читаем данные от MAX
        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        # Проверяем команду /start
        if data.get('text') == '/start':
            chat_id = data['chat']['id']
            self.send_welcome(chat_id, TOKEN, WEB_APP_URL, API_URL)
        
        # Отвечаем OK
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'ok': True}).encode())
    
    def send_welcome(self, chat_id, token, web_app_url, api_url):
        message = """🥜 Добро пожаловать в «Сладкий уголок»!

🌰 Орехи, сухофрукты и сладости в Кирове
✨ Только свежие продукты
🚚 Доставка за 24 часа

💰 Цены от 33₽ за 100гр

📍 Адрес: Кирово-Чепецкий район, ул. Ботаническая д.6

👇 Нажмите кнопку чтобы заказать:
"""
        
        data = {
            'chat_id': chat_id,
            'text': message,
            'reply_markup': {
                'keyboard': [[{
                    'text': '🛒 Открыть каталог',
                    'web_app': {'url': web_app_url}
                }]],
                'resize_keyboard': True
            }
        }
        
        try:
            url = f'{api_url}/{token}/sendMessage'
            requests.post(url, json=data)
        except Exception as e:
            print(f'Ошибка: {e}')
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot is running! ✅')