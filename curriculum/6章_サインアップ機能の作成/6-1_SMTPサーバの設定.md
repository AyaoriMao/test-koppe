# SMTPサーバの登録

## SMTPサーバとは
SMTPサーバーはメールの送信(配送)の際に必要となるサーバーです。
詳しくは[参考リンク](https://wa3.i-3-i.info/word1131.html)

## Djangoにおけるメール送信について
DjangoではSMTPサーバの情報とログイン情報を指定してやることでメール送信を非常に簡単に行うことができます。この章ではサインアップ時に本登録用リンクを送るような機能を実装するため、あらかじめSMTPサーバの情報を登録してやる必要があります。ただし、開発中に関してはわざわざSMTPサーバを用意してメールを送っていると動作確認に時間がかかってしまうため、当面はメールの内容をコンソールに表示するように設定しておきましょう。

settings.pyを以下の項目を追加します。

```py
## 中略 ##
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
## 中略 ##
```
これで、Djangoでメール送信を行うと、コンソール上にその内容が表示されるようになりました。

実際のSMPTサーバ設定はまた後程説明することとして、次に進みましょう。

以上で今回のパートは終了です。

お疲れ様でした。
