from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Это для подтверждения от VK
VK_CONFIRMATION_CODE = '7ffc3696'  # ← Вставь код из скрина!

@app.route('/vk', methods=['POST'])
def vk_handler():
    data = request.json
    
    # Если VK просит подтверждение
    if data.get('type') == 'confirmation':
        return VK_CONFIRMATION_CODE
    
    # Если новое сообщение
    if data.get('type') == 'message_new':
        user_id = data['object']['message']['from_id']
        text = data['object']['message']['text'].lower()
        
        if text in ['/start', 'старт', 'начать', 'привет']:
            # Здесь потом добавим отправку приветствия
            print(f"Пользователь {user_id} написал /start")
    
    return 'ok'

@app.route('/')
def index():
    return 'VK Бот работает! ✅'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))