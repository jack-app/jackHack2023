from flask import Flask, request
from flask_cors import CORS
import chat
import image

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "https://floral-gifter.netlify.app/"}})

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':

        req = request.get_json()
        content = req["content"]
        print(content)

        # こきくんがやってくれる、chatGPTの関数に値を渡す処理
        flower_info = chat.chat(content)
        if(type(flower_info) != dict):
            return "回答生成に失敗しました", 500

        # えんぴつくんがやってくれる、画像検索から画像のurlを取得する処理
        image_url = image.image(flower_info["name"])

        # エラー処理
        if(image_url == 0):
            return "画像検索に失敗しました", 500

        flower_info["image"] = image_url
        return flower_info

if __name__ == '__main__':
    app.run()