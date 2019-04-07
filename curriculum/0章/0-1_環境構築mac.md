# 開発を進める上で必要なツール（Mac）
このパートでは開発を進める上で必要なツールを紹介します。ここで紹介しているツールはあくまで私のおすすめなツールなので、ご自身で慣れているツール等を既にお使いであればこのパートは読み飛ばしても構いません。初めてテキストエディタやターミナルを使う方は是非参考にしてください。

**※）今回のパートはPCがMacの方を対象としています。**

**※）既にお手元のMacにエディタがある方はこちらのパートを読み飛ばして構いません。**

Windowsの方は「0-4 Cloud9を利用する手順」でCloud9の導入方法を記載しておりますのでこちらを参考にしてください。

[Cloud9を利用する手順]()


## テキストエディタ
プログラミングをしていく上で必要であるテキストエディタを準備します。

テキストエディタとは、テキストファイルを作成・編集・保存するためのソフトウェアです。


## Visual Studio Code
本講座ではVisual Studio CodeというMicrosoftが開発したオープンソースのテキストエディタの導入方法を説明していきます。Visual Studio Codeは通称VSCodeと呼ばれ、無料で利用できます。


## Visual Studio Codeの導入方法
ではVisual Studio Codeのインストール方法を説明していきます。

まず以下のリンクからVisual Studio Codeをダウンロードしてください。

[Visual Studio Codeのダウンロードページ](https://code.visualstudio.com/)

![image](https://i.gyazo.com/ca6d0a41c2d143a8b5053503363909e9.png)

ダウンロードが完了したらダウンロードしたファイルを展開してください。そのあと展開したファイルをアプリケーションフォルダに移動してください。移動させる方法色々ありますが、下記の動画ではFinderを2つ開いてドラック&ドロップで移動させています。(Finderを2つ開くには、Finderを開いた状態で`command + N`を押すことで2つ開くことができます。)

![image](https://i.gyazo.com/917887a28214f07429f731b61f49a114.gif)

アプリケーションフォルダに移動できたら、Visual Studio Codeを起動してください。下記の画面のようになっていればうまく導入ができています。

![image](https://i.gyazo.com/3a9c885cbe0dbf2758f7162c859f569d.png)

## Visual Studio Codeをカスタマイズ
デフォルトでもプログラミングはできますが、より開発しやすくするためにカスタマイズをしていきます。

**※)カスタマイズに関してはお好みで設定されて大丈夫です。**

まず、`Command + ,`を押して設定画面を開きます。

![image](https://i.gyazo.com/3f73f9773290bcd25ded645ff3f35427.png)

開いたら、下にスクロールをしていって、`Edit in settings.json`をクリックしてください。クリックしたらsettings.jsonファイルが展開されます。

![image](https://i.gyazo.com/61adc05697a618deb2d9d5f737dee53f.gif)

次に`settings.json`ファイルに以下のコードをコピーして、すでに書いてあるコードに上書きして保存してください。`command + S`で保存できます。（下記に示しているコードは、特に理解する必要はありません。）

```json
{
    // 差分を横に並べて表示ではなく行内に表示する
    "diffEditor.renderSideBySide": false,
    // ファイルを保存時に自動フォーマットする
    "editor.formatOnSave": true,
    // 現在の行を強調表示する
    "editor.renderLineHighlight": "all",
    // 空白文字を表示する。
    "editor.renderWhitespace": "all",
    // スペース2個インデント
    "editor.tabSize": 2,
    // ウィンドウ幅右端で折り返す
    "editor.wordWrap": "on",
    // ファイル保存時に最新の行を末尾に挿入する
    "files.insertFinalNewline": true,
    // アイコンテーマの指定
    "workbench.iconTheme": "vscode-icons"
}
```

上記のコードを追加したら下記の画像のように空白文字に「・・・・」と表示されていればカスタマイズがうまくできています。

![image](https://i.gyazo.com/02b74ac567ed7249b426a9d8e92bf685.png)

今回カスタマイズした内容はVSCodeを使っていくなかでお好みに変更されても構いません。


## 拡張機能の追加
より開発しやすくするために拡張機能を追加していきます。
追加する拡張機能は以下の3つです。

```
● Ruby
VSCodeに対するRuby言語とデバッグサポートを提供。
● Japanese Language Pack for Visual Studio Code
VSCodeを日本語に対応したUIを提供。
● vscode-icons
ファイルやフォルダにアイコンを追加。
```

では拡張機能を追加していきます。下記の画像のように左側にあるアイコンをクリックしてください。

![image](https://i.gyazo.com/b632f955a063c851c4b76315c2e13e4c.png)

すると拡張機能のMARKETPLACEが表示されるので、検索バーからインストールしたい拡張機能を検索しましょう。

![image](https://i.gyazo.com/182e29f848be2617b979606d4ae0dcd5.png)

(まずは試しにRubyと検索してみましょう。)

すると下記の画像のようにRubyの拡張機能が表示されるのでインストールしてください。

![image](https://i.gyazo.com/53bc02340dd67abd8c2b1a2cf8c63aa0.png)

これでRubyの拡張機能がインストールできました。同じやり方で他の拡張機能もインストールしてみましょう。

全てインストールできたらVSCodeを**再起動**してください。再起動することで拡張機能が使えるようになります。


## ターミナル
ターミナルとは、コマンドと呼ばれる命令文を用いてMacの操作や設定を行うためのツールです。ターミナルに関しては、Macにはデフォルトで用意されているので、インストールする必要はありません。ターミナルはコマンドを入力する際に利用します。

見た目をかっこよくするためにターミナルをカスタマイズすることもできますが、[Hyper](https://hyper.is/)というツールもおすすめです。

またVSCodeにもターミナルはあります。下記の動画のようにVSCodeの下部をクリックするとターミナルを表示できます。なのでVSCode内にあるターミナルを利用してコマンドを実行することもできます。

![image](https://i.gyazo.com/7abaa72bf4a755af90822a45717798c9.gif)

以上で今回のパートは終了です。

お疲れ様でした。