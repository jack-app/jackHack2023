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
        {"role": "system", "content": 'あなたは花を送りたい相手と、伝えたい気持ちから、送るべき花の名前と、花言葉と花を渡す際の例文を返すbotです。json形式で出力してください。それ以外の言葉は発さないでください。'},
        {"role": "system", "content": "json形式で出力してください。それ以外の言葉は発さないでください。花の名前をname,花言葉をflower_symbolism,例文をexampleとする"},
         {"role": "system", "content": f"{content['opponent']}さんに{content['feeling']}という気持ちを伝えたいとします"},
                ]
    )
    # parsed_response = json.loads(response.choices[0]["message"]["content"])
    # name = parsed_response['name']
    # flower_symbolism = parsed_response['flower_symbolism']
    # example = parsed_response['example']

    # print(bytes(response["choices"][0]["message"]["content"], encoding="utf-8").decode("utf-8"))
    # print(response.choice[0]["message"]["content"].strip())
    # 結果を辞書形式で返す
    # return {
    #     "name": name,
    #     "flower_symbolism": flower_symbolism,
    #     "example": example
    # }
    responsefix = bytes(response["choices"][0]["message"]["content"], encoding="utf-8").decode("utf-8")
    result = json.loads(responsefix)
    print(result)
    # result = {
    #     "name": name,
    #     "flower_symbolism": flower_symbolism,
    #     "example": example
    # }

    return result
    
    # contentの中身はこんな感じ。main.pyから渡されるよ。
    """
    content = {
      "opponent": "お母さん",
      "feeling": "感謝の気持ち"
    }
    """
    
    print(content["opponent"])
    print(content["feeling"])

    # ここに入力を受け取ってchatGPTのAPIの処理を書いてね
    # 以下に示した例みたいな形でreturnすることができたらok!
    # chatGPTのAPIにどのように渡せばいいか工夫してやってみよう！
    
    # 返すものの例
    return {
	    "name": "ひまわり",
	    "flower_symbolism": "いつもあなたを向いています",
	    "example": "ひまわりのように、いつもあなたのことを一途に考えています。"
    }

if __name__ == '__main__':
    chat(None)