# ここにchatGPTの検索の処理を書いてね
import openai
import json

openai.api_key = "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"

situation = input("状況を入力してください： ")
age = input("年齢を入力してください： ")
recipient = input("誰に渡すか入力してください： ")

model_engine = "text-davinci-002"
prompt = f"花を選ぶための条件：状況は「{situation}」、年齢は「{age}」、誰に渡すかは「{recipient}」です。"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

flower_name = completions.choices[0].text.strip()

response = openai.Completion.create(
    engine=model_engine,
    prompt=f"花の花言葉と画像を取得する：{flower_name}",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

result = json.loads(response.choices[0].text)

print(json.dumps(result))