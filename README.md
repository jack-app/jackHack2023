# Floral Gifter

<img width="636" alt="スクリーンショット 2023-05-06 0 02 47" src="https://user-images.githubusercontent.com/83484258/236495330-d3fc283a-02e2-403a-8a99-65c058550877.png">

## overview

花を渡したい相手と、伝えたい思いを入力することで、どんな花を渡せばいいかを花言葉を踏まえた例文をもとに返してくれます。

URL：https://floral-gifter.netlify.app/

発表スライド：https://www.canva.com/design/DAFiAQfU-tA/LR6Al14IExb_XVhKo_QuIA/view?utm_content=DAFiAQfU-tA&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink

### setup

### frontend

1. パッケージをインストールする

```
npm install
```

2. ホスティング

```
npm run dev
```

### backend

1. パッケージのインストール

```
pip install -r requirements.txt
```

2. ホスティング

開発環境の場合

```
python3 main.py 
```
本番環境の場合
```
gunicorn main:app
```
