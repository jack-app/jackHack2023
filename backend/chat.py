import io, sys
import json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
# ここにchatGPTの検索の処理を書いてね
import openai

# OpenAI APIを設定
openai.api_key = "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"
model_engine = "text-davinci-002"


def chat(content):
    content = {
      "opponent": "お母さん",
      "feeling": "感謝の気持ち"
    }
    # GPT-3にプロンプトを送信して結果を取得する
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": 'あなたは花を送りたい相手と、伝えたい気持ちから、送るべき花の名前と、花言葉と、花を渡す際の例文を返すアプリです。その出力をそれぞれスペースで区切って入力してください。それ以外の言葉は発さないでください。'},
        {"role": "user", "content": f"{content['opponent']}さんに{content['feeling']}という気持ちを伝えたいです。"},
      ]
    )

    responsefix = bytes(response["choices"][0]["message"]["content"], encoding="utf-8").decode("utf-8")
    print(responsefix)
    print(type(responsefix))
    # result = {
    #     "name": name,
    #     "flower_symbolism": flower_symbolism,
    #     "example": example
    # }

    return result
    

if __name__ == '__main__':
    chat(None)