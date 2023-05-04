import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
# ここにchatGPTの検索の処理を書いてね
import openai
import os
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")

# OpenAI APIを設定
openai.api_key = os.environ.get("OPENAI_API_KEY")
model_engine = "text-davinci-002"


def chat(content):
    # GPT-3にプロンプトを送信して結果を取得する
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": 'あなたは花を送りたい相手と、伝えたい気持ちから、送るべき花の名前と、花言葉と、花を渡す際の例文を返すアプリです。その出力をそれぞれスペースで区切って入力してください。それ以外の言葉は発さないでください。'},
        {"role": "user", "content": f"{content['opponent']}さんに{content['feeling']}という気持ちを伝えたいです。"},
      ]
    )

    responsefix = bytes(response["choices"][0]["message"]["content"], encoding="utf-8").decode("utf-8")
    responsefix1 = list(map(str,responsefix.split()))
    print(responsefix1)
    result = {
        "name" : responsefix1[0],
        "flower_symbolism" : responsefix1[1],
        "example" : responsefix1[2]
    }
    print(result)
    print(type(result))
    # result = {
    #     "name": name,
    #     "flower_symbolism": flower_symbolism,
    #     "example": example
    # }

    return result
    

if __name__ == '__main__':
    chat(None)