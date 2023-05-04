# ここに画像検索のAPIを叩く処理を書いてね
#ライブラリのインポート
from requests import get,post
from json import loads
import os 
from os.path import dirname, join
from datetime import datetime
from requests_oauthlib import OAuth1

from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")

#環境変数の読み込み
CUSTOM_SEARCH_API_KEY = os.environ.get("CUSTOM_SEARCH_API_KEY")
CUSTOM_SEARCH_ENGINE_ID = os.environ.get("CUSTOM_SEARCH_ENGINE_ID")
UNSPLASH_API_ACCESS_KEY = os.environ.get("UNSPLASH_API_ACCESS_KEY")

TRANSLATOR_API_KEY=os.environ.get("TRANSLATOR_API_KEY")
TRANSLATOR_API_SECRET=os.environ.get("TRANSLATOR_API_SECRET")
TRANSLATOR_API_USERNAME=os.environ.get("TRANSLATOR_API_USERNAME")

#定数の設定
HOWMANY = 1
ASPECTRATE = "4:3" #横:縦
API = "google"#unsplash/google

#アカウントの取得がうまくできず断念.
"""
#画像検索APIにBing Image Searchを用いる場合

def bing(flower_name):
    try:
        result,status = query("https://api.cognitive.microsoft.com/bing/v7.0/images/search",
                    {"Ocp-Apim-Subscription-Key":KEYS["Bing Search API"]["SubscriptionKey"]},
                    {
                    "license":"public",
                    "q":f"(flower|花) {flower_name}",
                    "imageType":"photo",
                    "count":HOWMANY,
                    "aspect":"All"
                    }
                    )
    #https://learn.microsoft.com/ja-jp/bing/search-apis/bing-image-search/reference/query-parameters
    except:
        return 0
    if status == 1:
        return 0
    return result
"""


#画像検索APIにCustom search APIを用いる場合

def google(flower_name):
    #Custom search APIに画像を要求
    try:
        result = get("https://customsearch.googleapis.com/customsearch/v1",
                    headers={},
                    params={
                    "key":CUSTOM_SEARCH_API_KEY,
                    "cx":CUSTOM_SEARCH_ENGINE_ID,
                    "q":f"(flower|花) {flower_name}",
                    "fileType":"jpeg png jpg",
                    "searchType":"image",
                    "imgType":"photo",
                    "imgSize":"xlarge",
                    "num":HOWMANY
                    }
                    )
    #https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list?hl=ja
    except:
        return 0
    if result.status_code != 200:
        return 0
    
    #抽出返答
    return loads(result.content)["items"][0]["link"]



def translate(word):
    #少々応答が遅いのがネック
    try:
        result = post("https://mt-auto-minhon-mlt.ucri.jgn-x.jp/api/mt/generalNT_ja_en/",
                    data={
                        "key":TRANSLATOR_API_KEY,
                        "name":TRANSLATOR_API_USERNAME,
                        "type":"json",
                        "text":word
                    },
                    auth=OAuth1(
                        TRANSLATOR_API_KEY,
                        TRANSLATOR_API_SECRET
                    )
                    )
    except:
        return 0
    if result.status_code != 200:
        return 0
    return result.json()["resultset"]["result"]["text"]

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

    #unsplashで検索するために英語に変換
    flower_name=translate(flower_name)

    print(f"get:{flower_name}")
    #クエリを使い果たしたらリクエストを投げない。
    if not request_is_vailed:
        if last_update != datetime.now().hour:
            last_update = datetime.now().hour
        else:
            return 0

    #unsplashAPIに{flower_name}の写真を要求
    try:
        result = get("https://api.unsplash.com/photos/random/",
                    params={
                    "client_id":UNSPLASH_API_ACCESS_KEY,
                    "query":flower_name,
                    "count":HOWMANY
                    }
                    )
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



def _shift_to_front(list_,element):
    list_.remove(element)
    list_.insert(0,element)

def image(flower_name):
    try_order = [google,unsplash]
    if API=="unsplash":
        _shift_to_front(try_order,unsplash)
    elif API=="google":
        _shift_to_front(try_order,google)
    """
    elif API=="bing":
        return bing(flower_name)
    """

    #複数のAPIを叩けるように処理
    res = 0
    for f in try_order:
        res = f(flower_name)
        if res != 0:
            break
    return res

if __name__ == "__main__":
    print(translate("sunflower"))
    print(unsplash("sunflower"))