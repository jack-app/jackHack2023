# ここに画像検索のAPIを叩く処理を書いてね
#ライブラリのインポート
from requests import get
from json import load,loads
from os import chdir,getcwd
from os.path import dirname
from datetime import datetime

#定数の設定
HOWMANY = 1
ASPECTRATE = "4:3" #横:縦
API = "unsplash"#unsplash/
#Jsonの読み込み
if __name__ == "__main__":
    chdir(dirname(__file__))
    print(getcwd())
with open("UnsplashAPIkey.json") as f:
    KEYS = load(f)


#画像検索APIにunsplashを用いる場合

#サーバーの起動中保持する変数を設定
last_update = datetime.now().hour
request_is_vailed = True

def unsplash(flower_name):
    """花の写真を指すurlを返します。
    flower_nameは必ず英名の文字列を渡してください。
    何らかのエラーにより画像を取得できなかった場合はintの0を返します。
    """
    global last_update,request_is_vailed

    print(f"get:{flower_name}")
    #クエリを使い果たしたらリクエストを投げない。
    if not request_is_vailed:
        if last_update != datetime.now().hour:
            last_update = datetime.now().hour
        else:
            return 0

    #unsplashAPIに{flower_name}の写真を1つ要求
    try:
        result = get("https://api.unsplash.com/photos/random/?"
                 +f"client_id={KEYS['Unsplash']['AccessKey']}"
                 +f"&query=\"{flower_name}\""
                 +f"&count={HOWMANY}")
    except:
        return 0

    if result.status_code != 200:
        return 0
    
    #結果から画像URLを抽出
    parsed_result = loads(result.text)
    raw_image_url = parsed_result[0]["urls"]["raw"]

    #残りクエリ回数を確認
    print("UnsplashAPI: X-Ratelimit-Remaining:",result.headers["X-Ratelimit-Remaining"])
    if result.headers["X-Ratelimit-Remaining"]==0:
        request_is_vailed = False

    #APIの機能を用いて画像を成形
    #refer "https://unsplash.com/documentation#supported-parameters"
    image_url = raw_image_url + f"&ar={ASPECTRATE}&crop=entropy&fit=crop"

    return image_url




def image(flower_name):
    if API=="unsplash":
        return unsplash(flower_name)


if __name__ == "__main__":
    print(image("flower blue rose"))