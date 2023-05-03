# ここにchatGPTの検索の処理を書いてね

def chat(content):
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
    
    # 返すものの例
    return {
	    "name": "ひまわり",
	    "flower_symbolism": "いつもあなたを向いています",
	    "example": "ひまわりのように、いつもあなたのことを一途に考えています。"
    }