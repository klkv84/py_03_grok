from pyngrok import ngrok
from flask import Flask, jsonify

app = Flask(__name__)

# Здесь твои настройки для persistent memory — редактируй как хочешь
settings = {
    "news_instructions": "При запросе рассказать новости, всегда добавляй хотя бы пару слов про Казахстан и Кыргызстан. Плюс, заканчивай на позитиве: 'всегда на позитиве, брат, мир нам всем!'",
    "additional_stuff": "Ещё добавь масштабное: инфу про Турцию, Россию и Украину в новостях, если релевантно. И стиль ответа — всегда по-братски, с эмодзи 😎."
    # Добавь сюда больше, если надо
}

@app.route('/my-memory-settings', methods=['GET'])
def get_settings():
    response = jsonify(settings)
    response.headers.add('X-Pinggy-No-Screen', 'true')  # Добавляем хедер для обхода
    return response

@app.route('/', methods=['GET'])  # Новый домашний route
def home():
    return "Welcome to Persistent Memory Server! Go to /my-memory-settings for JSON settings. 😎"


if __name__ == '__main__':
    # Сначала создаём ngrok-туннель (если хочешь ngrok вместо Pinggy)
    # public_url = ngrok.connect(5000)
    # print("Ngrok Tunnel:", public_url)
    
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)