from flask import Flask, abort, request
from flask_cors import CORS
import chat
import image

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
      
      req = request.get_json()
      content = req["content"]
      print(content)

      # こきくんがやってくれる、chatGPTの関数に値を渡す処理
      flower_info = chat.chat(content)
      

      # えんぴつくんがやってくれる、画像検索から画像のurlを取得する処理
      image_url = image.image(flower_info["name_en"])

      # エラー処理
      if(image_url == 0):
          abort(404)
      
          
      flower_info["image"] = image_url
      return flower_info

if __name__ == '__main__':
    app.run()