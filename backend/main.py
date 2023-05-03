from flask import Flask
import chat

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    content = {
        "opponent": "お母さん",
        "feeling": "感謝の気持ち"
    }
    aaa = chat.chat(content)

    return aaa

if __name__ == '__main__':
    app.run()