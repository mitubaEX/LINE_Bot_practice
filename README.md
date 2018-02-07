# LINE_Bot_practice
制作合宿用的な

## Usage

env_var.txtにLINEのトークンやTalkAPIのトークンを記入しよう．
できたら以下のコマンドでOK

```
$ docker-compose up

# after run server
$ ngrok http 5000
```

## install ngrok


- for mac

```
brew cask install ngrok
```

- other
https://ngrok.com/download

## install heroku
```
brew install heroku/brew/heroku
```

## heroku deploy

```
# heroku configuration
heroku container:login
heroku create

# push
docker build -t server .
docker tag server registry.heroku.com/<your app>/web
docker push registry.heroku.com/<your app>/web
```
