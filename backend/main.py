from flask import Flask, render_template, request
import chat
import image

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
      
      content = request.form["content"]

      # こきくんがやってくれる、chatGPTの関数に値を渡す処理
      flower_info = chat.chat(content)
      

      # えんぴつくんがやってくれる、画像検索から画像のurlを取得する処理
      image_url = image.image(flower_info["name_en"])

      # エラー処理
      if(image_url == 0):
          return "error!"
      
      else:
          
          flower_info["image"] = image_url
          return flower_info

if __name__ == '__main__':
    app.run()