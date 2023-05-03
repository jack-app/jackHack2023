# ここに画像検索のAPIを叩く処理を書いてね
#ライブラリのインポート
from requests import get
from json import load,loads
from os import chdir,getcwd
from os.path import dirname

#定数の設定
HOWMANY = 1
ASPECTRATE = "4:3" #横:縦

#Jsonの読み込み
if __name__ == "__main__":
    chdir(dirname(__file__))
    print(getcwd())
with open("UnsplashAPIkey.json") as f:
    KEYS = load(f)

def image(flower_name):
    """花の写真を指すurlを返します。
    flower_nameは必ず英名の文字列を渡してください。
    何らかのエラーにより画像を取得できなかった場合はintの0を返します。
    """

    #unsplashAPIに{flower_name}の写真を1つ要求
    try:
        result = get("https://api.unsplash.com/photos/random/?"
                 +f"client_id={KEYS['AccessKey']}"
                 +f"&query={flower_name}"
                 +f"&count={HOWMANY}")
    except:
        return 0

    if result.status_code != 200:
        return 0
    
    parsed_result = loads(result.text)

    raw_image_url = parsed_result[0]["urls"]["raw"]

    #APIの機能を用いて画像を成形
    #refer "https://unsplash.com/documentation#supported-parameters"
    image_url = raw_image_url + f"&ar=4:3&crop=entropy&fit=crop"

    return image_url

if __name__ == "__main__":
    print(image("Iris"))