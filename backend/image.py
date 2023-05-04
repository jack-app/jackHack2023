# ここに画像検索のAPIを叩く処理を書いてね
#ライブラリのインポート
from requests import get,Response
from json import load,loads
from os import chdir,getcwd
from os.path import dirname
from datetime import datetime

#定数の設定
HOWMANY = 1
ASPECTRATE = "4:3" #横:縦
API = "google"#unsplash/google/bing
#Jsonの読み込み
if __name__ == "__main__":
    chdir(dirname(__file__))
    print(getcwd())
with open("APIkey.json") as f:
    KEYS = load(f)



def query(url):
    result = get(url)
    if result.status_code != 200:
        print(result.status_code)
        print(result.reason)
        return result,1
    return result,0



#画像検索APIにCustom search APIを用いる場合

def google(flower_name):
    #Custom search APIに画像を要求
    try:
        result,status = query("https://customsearch.googleapis.com/customsearch/v1?"
                     +f"key={KEYS['Custom Search API']['APIKey']}"
                     +f"&cx={KEYS['Custom Search API']['SearchEngineID']}"
                     +f"&q='(flower|花) {flower_name}'"
                     +"&fileType='jpeg png jpg'"
                     +"&searchType=image"
                     +"&imgType=photo"
                     +"&imgSize=xlarge"
                     +"&num=1"
                     )
    except:
        return 0
    if status == 1:
        return 0
    
    #抽出返答

    return loads(result.content)["items"][0]["link"]



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
        result,status = query("https://api.unsplash.com/photos/random/?"
                    +f"client_id={KEYS['Unsplash']['AccessKey']}"
                    +f"&query=\"{flower_name}\""
                    +f"&count={HOWMANY}")
    except:
        return 0
    if status == 1:
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
    elif API=="google":
        return google(flower_name)


if __name__ == "__main__":
    print(image("blue rose"))