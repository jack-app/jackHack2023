from flask import Flask, request
import chat
import image

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
      # TO:ちょうくん
      # POSTリクエストで、contentという名前で、json形式のデータが送られてくるよ
      content = request.form["content"]

      # 受け取る処理を書いてみよう。


      # こきくんがやってくれる、chatGPTの関数に値を渡す処理
      flower_info = chat.chat(content)

      # TO:ちょうくん
      # flower_infoから、花の名前を取得して、image関数に渡してね
      """flower_infoの中身はこんな感じのが入ってるよ
      {
        "name": "ひまわり",
        "flower_symbolism": "いつもあなたを向いています",
        "example": "ひまわりのように、いつもあなたのことを一途に考えています。"
      }
      """
      flower_name = flower_info["name_en"]
      

      # えんぴつくんがやってくれる、画像検索から画像のurlを取得する処理
      image_url = image.image(flower_name)

      # TO:ちょうくん
      # ここで、flower_infoとimage_urlを組み合わせて、json形式で返してね
      # 以下の例みたいな形でreturnすることができたらok!
      """
      {
        "name": "ひまわり",
        "flower_symbolism": "いつもあなたを向いています",
        "image": "https://hogehoge.com",
        "example": "ひまわりのように、いつもあなたのことを一途に考えています。"
      }
      """
      flower_info["image"] = image_url

      return flower_info

if __name__ == '__main__':
    app.run()