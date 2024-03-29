# 他ページとの紐付け
このパートでは、商品詳細画面→ショッピングカート画面というユースケースを想定し、ショッピングカート画面へPOSTするフォームを商品詳細画面へ追加し、またショッピングカート画面のJavascriptで数量変更、削除を行えるよう実装します。またログインへのリンクをベーステンプレートに追加したように、ショッピングカートへのリンクもベーステンプレートに追加します。

## ベーステンプレートにショッピングカート画面へのリンク追加
修正するのはベーステンプレート(base.html)です。
```
techpit/
　 ├ amazon/
　 ├ static/
　 ├ manage.py
　 ├ templates/ 
 　　└ amazon/ 
    　 ├ ・・・
　     ├ base.html #修正
　　　　・・・
```

base.htmlへショッピングカート画面へのリンクを追加します。
```html
{% load static %}
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" >
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
    <link href="{% static 'css/base.css' %}" rel="stylesheet" type="text/css"/>
    <link href="{% static 'css/responsive.css' %}" rel="stylesheet" media="only screen and (max-width: 1200px)" />
    <script src="{% static 'js/script.js' %}" type="text/javascript"></script>

    <title>techpit amazon</title>
    <body>
        <header class="section-header">
            <section class="header-main">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-md-3">
                        <a href="{% url 'amazon:lp' %}">
                            <div class="brand-wrap">
                                <img class="logo" src="{% static 'images/logo-dark.png' %}">
                                <h2 class="logo-text">Techpit amazon</h2>
                            </div> <!-- brand-wrap.// -->
                        </a>
                        </div>
                        <div class="col-lg-6 col-sm-6">
                            <form method= "get" action="{% url 'amazon:item_list' %}" class="search-wrap">
                                <div class="input-group">
                                    <input name="q" type="text" class="form-control" placeholder="Search">
                                    <div class="input-group-append">
                                        <button id="id_search_button" class="btn btn-warning" type="submit">
                                        <i class="fa fa-search"></i>
                                        </button>
                                    </div>
                                </div>
                            </form> <!-- search-wrap .end// -->
                        </div> <!-- col.// -->
                        <div class="col-lg-3 col-sm-6">
                            <div class="widgets-wrap d-flex justify-content-end">
                                <!-- [7-5 追加] リンク追加 ここから -->
                                {% if user.is_authenticated %}
                                <div class="widget-header icontext">
                                    <a href="{% url 'amazon:cart' user.cart.pk %}" class="icontext">
                                        <div class="icon-wrap icon-sm bg2 round text-secondary"><i class="fa fa-shopping-cart"></i></div>
                                        <div class="text-wrap">
                                            <small>カート</small>
                                            <span>{{ user.cart.item_count|default_if_none:"0" }}商品</span>
                                        </div>
                                    </a>
                                </div> <!-- widget .// -->
                                {% endif %}
                                <!-- [7-5 追加] リンク追加 ここまで -->
                                <!-- [5-6 追加/修正] ログイン状態による分岐 ここから -->
                                <div class="widget-header icontext">
                                    <div class="icon-wrap icon-sm bg2 round text-secondary"><i class="fa fa-user"></i></div>
                                    <div class="text-wrap">
                                        {% if user.is_authenticated %}
                                        <small>{{user.name}}さん</small>
                                        <span><a href="{% url 'amazon:logout' %}">Logout</a></span>
                                        {% else %}
                                        <small>ゲスト</small>
                                        <span><a href="{% url 'amazon:login' %}">Login</a></span>
                                        {% endif %}
                                    </div>
                                </div> <!-- widget  dropdown.// -->
                                <!-- [5-6 追加/修正] ログイン状態による分岐 ここまで -->
                                
                            </div>	<!-- widgets-wrap.// -->	
                        </div> <!-- col.// -->
                    </div> <!-- row.// -->
                </div> <!-- container.// -->
            </section> <!-- header-main .// -->
        </header> <!-- section-header.// -->
        <div class="container" style="padding: 2rem">
                {% block content %}{% endblock %}
        </div>
        <footer class="section-footer bg2">
            <div class="container">
                <section class="footer-bottom row">
                    
                    <div class="col-sm-12">
                        <p class="text-sm-right">
        Copyright &copy 2019 
        <a href="#">Techpit</a>
                        </p>
                    </div>
                </section> <!-- //footer-top -->
            </div><!-- //container -->
        </footer>
         {% block scripts %}{% endblock %}
    </body>
</html>
```

ここではログイン画面へのリンクを追加した時と同様に、ショッピングカート画面へのリンクをベーステンプレートのヘッダ部分に表示しております。またショッピングカート画面はログイン必須ですので、`if is_authenticated` でログイン時のみ表示しております。

新たに出てきた構文を解説します。
* `{{ xxx|default_if_none:yyy }}`
    * xxxがNoneである場合はyyyと表示するという記法です。このようにコンテキストに対して"|"を挟んで処理を被せる機能をフィルタと呼び、今回のdefaut_if_noneはデフォルトで用意されているフィルタのうちの一つになります。


## ショッピングカートへ追加する機能
修正するのは商品詳細画面のテンプレートファイル(item_detail.html)です。

```
techpit/
　 ├ amazon/
　 ├ static/
　 ├ manage.py
　 ├ templates/ 
 　　└ amazon/ 
    　 ├ ・・・
　     ├ item_detail.html #修正
　　　　・・・
```

item_detail.htmlに”カートに追加ボタン”を追加します。
```html
{% extends "amazon/base.html" %}
{% block content %}
{% load static %}

<main class="mt-5 pt-4">
    <div class="container dark-grey-text mt-5">
        <div class="row wow fadeIn">
            <div class="col-md-6 mb-4">
                <img src="{{ object.thumbnail.url }}" class="img-fluid" alt="">
            </div>
            <div class="col-md-6 mb-4">
                <div class="p-4">
                    <div class="mb-3">
                        <a href="">
                        <span class="badge purple mr-1">Category 2</span>
                        </a>
                        <a href="">
                        <span class="badge blue mr-1">New</span>
                        </a>
                        <a href="">
                        <span class="badge red mr-1">Bestseller</span>
                        </a>
                    </div>
                    <p class="lead">
                        <h2>{{ object.name }}</h2>
                        <span>¥{{ object.price }}</span>
                    </p>

                    <p class="lead font-weight-bold">商品説明</p>
                    <p>{{ object.description }}</p>
                    
                    <!--  [7-5 追加]カートに追加ボタン ここから -->
                    {% if user.is_authenticated %}
                    <form method="post" action="{% url 'amazon:cart' user.cart.pk %}" class="d-flex justify-content-left">
                        {% csrf_token %}
                        <!-- Default input -->
                        <input name="product_pk" type="hidden" value="{{ object.pk }}">
                        <input name="amount" type="number" value="1" aria-label="Search" class="form-control" style="width: 100px; margin-right: 1rem">
                        <button class="btn btn-primary btn-md my-0 p" type="submit">Add to cart
                        <i class="fas fa-shopping-cart ml-1"></i>
                        </button>
                    </form>
                    {% endif %}
                     <!--  [7-5 追加]カートに追加ボタン ここまで -->
                </div>
            </div>
        </div>
        <hr>
        <div class="row d-flex justify-content-center wow fadeIn">
            <div class="col-md-6 text-center">
                <h4 class="my-4 h4">Additional information</h4>
                <p>
                    Djangoのようなフレームワークを利用しても、ページのデザインを綺麗にすることはできません。
                    恐らくこの教材で学習している方のほとんどがどちらかというとサーバサイドを勉強している方が多いのかと思慮しますので、
                    htmlやcssの部分はあまり得意でないという方が多いと思います。そのような方はぜひBootstrap等のCSSフレームワークを利用することをお勧めします。
                    また、コードのスニペットをネット上から拝借するのも非常に良いと思います。日本の
                    サイトですとまだこのスニペットのまとめサイトのようなものは少ないですが、海外ですと無数に存在するので、ぜひそれらを活用していただくことをお勧めします。(無料で公開されていることろが多いです)
                    特にログイン画面やサインアップ部分は「bootstrap login snippet」等で検索するといろいろな方が作成したスニペットが出てくるので、是非今後「自分でサービス開発したい！」となった際にご参考にしていただければと思います。
                </p>
            </div>
        </div>
        <div class="row wow fadeIn">
            <div class="col-lg-4 col-md-12 mb-4">
                <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Products/11.jpg" class="img-fluid" alt="">

            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Products/12.jpg" class="img-fluid" alt="">
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Products/13.jpg" class="img-fluid" alt="">

            </div>
        </div>
    </div>
</main>   
{% endblock %}

```

## Ajax部分の実装
まず、サーバとの通信に必要なCSRFトークンをAjax通信の際にも利用できるよう記述する必要があるので、ベーステンプレート(techpit/templates/amazon/base.html)のJavascript部分を以下のように修正します。

base.htmlへAjax時のcsrfトークン対策追加
```html
{% load static %}
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" >
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
    <link href="{% static 'css/base.css' %}" rel="stylesheet" type="text/css"/>
    <link href="{% static 'css/responsive.css' %}" rel="stylesheet" media="only screen and (max-width: 1200px)" />
    <script src="{% static 'js/script.js' %}" type="text/javascript"></script>

    <title>techpit amazon</title>
    <body>
        <header class="section-header">
            <section class="header-main">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-md-3">
                        <a href="{% url 'amazon:lp' %}">
                            <div class="brand-wrap">
                                <img class="logo" src="{% static 'images/logo-dark.png' %}">
                                <h2 class="logo-text">Techpit amazon</h2>
                            </div> <!-- brand-wrap.// -->
                        </a>
                        </div>
                        <div class="col-lg-6 col-sm-6">
                            <form method= "get" action="{% url 'amazon:item_list' %}" class="search-wrap">
                                <div class="input-group">
                                    <input name="q" type="text" class="form-control" placeholder="Search">
                                    <div class="input-group-append">
                                        <button id="id_search_button" class="btn btn-warning" type="submit">
                                        <i class="fa fa-search"></i>
                                        </button>
                                    </div>
                                </div>
                            </form> <!-- search-wrap .end// -->
                        </div> <!-- col.// -->
                        <div class="col-lg-3 col-sm-6">
                            <div class="widgets-wrap d-flex justify-content-end">
                                <!-- [7-5] ショッピングカート画面へのリンク追加 ここから -->
                                {% if user.is_authenticated %}
                                <div class="widget-header icontext">
                                    <a href="{% url 'amazon:cart' user.cart.pk %}" class="icontext">
                                        <div class="icon-wrap icon-sm bg2 round text-secondary"><i class="fa fa-shopping-cart"></i></div>
                                        <div class="text-wrap">
                                            <small>カート</small>
                                            <span>{{ user.cart.item_count|default_if_none:"0" }}商品</span>
                                        </div>
                                    </a>
                                </div> <!-- widget .// -->
                                {% endif %}
                                <!-- [7-5] ショッピングカート画面へのリンク追加 ここまで -->
                                <!-- [5-6] ログイン状態による分岐追加 ここから -->
                                <div class="widget-header icontext">
                                    <div class="icon-wrap icon-sm bg2 round text-secondary"><i class="fa fa-user"></i></div>
                                    <div class="text-wrap">
                                        {% if user.is_authenticated %}
                                        <small>{{user.name}}さん</small>
                                        <span><a href="{% url 'amazon:logout' %}">Logout</a></span>
                                        {% else %}
                                        <small>ゲスト</small>
                                        <span><a href="{% url 'amazon:login' %}">Login</a></span>
                                        {% endif %}
                                    </div>
                                </div> <!-- widget  dropdown.// -->
                                <!-- [5-6] ログイン状態による分岐追加 ここまで -->
                                
                            </div>	<!-- widgets-wrap.// -->	
                        </div> <!-- col.// -->
                    </div> <!-- row.// -->
                </div> <!-- container.// -->
            </section> <!-- header-main .// -->
        </header> <!-- section-header.// -->
        <div class="container" style="padding: 2rem">
                {% block content %}{% endblock %}
        </div>
        <footer class="section-footer bg2">
            <div class="container">
                <section class="footer-bottom row">
                    
                    <div class="col-sm-12">
                        <p class="text-sm-right">
        Copyright &copy 2019 
        <a href="#">Techpit</a>
                        </p>
                    </div>
                </section> <!-- //footer-top -->
            </div><!-- //container -->
        </footer>
        <!-- [7-5] Ajax csrf対策追加 ここから -->
        <script type="text/javascript">
            function getCookie(name) {
               var cookieValue = null;
               if (document.cookie && document.cookie !== '') {
                   var cookies = document.cookie.split(';');
                   for (var i = 0; i < cookies.length; i++) {
                       var cookie = jQuery.trim(cookies[i]);
                       // Does this cookie string begin with the name we want?
                       if (cookie.substring(0, name.length + 1) === (name + '=')) {
                           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                           break;
                       }
                   }
               }
               return cookieValue;
           }

           var csrftoken = getCookie('csrftoken');

           function csrfSafeMethod(method) {
               // these HTTP methods do not require CSRF protection
               return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
           }

           $.ajaxSetup({
               beforeSend: function (xhr, settings) {
                   if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                       xhr.setRequestHeader("X-CSRFToken", csrftoken);
                   }
               }
           });   
       </script>
       <!-- [7-5] Ajax csrf対策追加 ここまで -->
         {% block scripts %}{% endblock %}
    </body>
</html>
```


引き続き、数量変更のAjax通信部分を実装していきます。
ショッピングカート画面のテンプレート(techpit/templates/amazon/shopping_cart.html)を修正します。

shopping_cart.htmlのAjax部分を実装します。
```html
{% extends "amazon/base.html" %}
{% block content %}
{% load static %}

{% if object.cart_items.all %}
 <div class="card shopping-cart">
    <div class="card-body">
        {% for cart_item in object.cart_items.all %}
        <div class="row">
            <div class="col-12 col-sm-12 col-md-2 text-center">
                    <img class="img-responsive" src="{{ cart_item.product.thumbnail.url }}" alt="prewiew" width="120" height="80">
            </div>
            <div class="col-12 text-sm-center col-sm-12 text-md-left col-md-6">
                <h4 class="product-name"><strong>{{ cart_item.product.name }}</strong></h4>
                <h4>
                    <small>{{ cart_item.product.description }}</small>
                </h4>
            </div> <!-- col -->
            <div class="col-12 col-sm-12 text-sm-center col-md-4 text-md-right row">
                <div class="col-3 col-sm-3 col-md-6 text-md-right" style="padding-top: 5px">
                    <h6><strong>{{ cart_item.product.price }} <span class="text-muted">x</span></strong></h6>
                </div>
                <div class="col-4 col-sm-4 col-md-4">
                    <div class="quantity">
                        <input name="amount" pk="{{ cart_item.pk }}" type="number" class="form-control" step="1" max="99" min="1" title="Qty" class="qty" size="4" value="{{ cart_item.amount }}"> 
                    </div>
                </div>
                <div class="col-2 col-sm-2 col-md-2 text-right">
                    <button name="delete" pk="{{ cart_item.pk }}" type="button" class="btn btn-outline-danger btn-xs">
                        <i class="fa fa-trash" aria-hidden="true"></i>
                    </button>
                </div>
            </div> <!-- col -->
        </div> <!-- row -->
        {% endfor %}
        <hr>
    </div> <!-- card body -->
    <div class="card-footer">
        <a href="" class="btn btn-success pull-right">Checkout</a>
        <div class="float-right">Total price: <b> ¥{{ object.total_price }}</b></div>
    </div>
    </div> <!-- card footer -->
</div> <!-- card -->
{% else %}
<p>カートが空です</p>
{% endif %}
{% endblock %}

<!-- [7-5] Ajaxリクエスト部分追加 ここから -->
{% block scripts %}
<script>
    function call_update_amount(_pk, _amount) {
        return $.ajax({
            url: '{% url "amazon:update_cart_item_amount" %}',
            type: 'POST',
            dataType: 'json',
            data: {
                cart_item_pk: _pk,
                amount: _amount
            }
        });
    }
    function call_delete_item(_pk) {
        return $.ajax({
            url: '{% url "amazon:delete_cart_item" %}',
            type: 'POST',
            dataType: 'json',
            data: {
                cart_item_pk: _pk
            }
        });
    }

    $(function() {
        var $input_amount = $('input[name="amount"]');
        var $delete_button = $('button[name="delete"]');
        $input_amount.on('change', function() {
            var cart_item_pk = $(this).attr('pk');
            var new_amount = parseInt($(this).val());
            call_update_amount(cart_item_pk, new_amount)
            .done((data) => {
                if (data.success) {
                    location.reload();
                    return;
                }
                alert(data.error);
            })
            .fail((ata, textStatus, xhr) => {
                alert(xhr);
            });
        });
        $delete_button.on('click', function() {
            var cart_item_pk = $(this).attr('pk');
            call_delete_item(cart_item_pk)
            .done((data) => {
                if (data.success) {
                    location.reload();
                    return;
                }
                alert(data.error);
            })
            .fail((ata, textStatus, xhr) => {
                alert(xhr);
            });
        });
    })
</script>
{% endblock %}
<!-- [7-5] Ajaxリクエスト部分追加 ここまで -->

```

上記は、数量変更および削除ビューと通信するAjax処理になります。
本教材の本質ではないため、詳しい解説は割愛します。


## 動作確認
まずはランディングページにアクセスします。
localhost:8000/techpit/amazon/lp

[![Image from Gyazo](https://i.gyazo.com/edf6f6bae7616c651ada838e0d4f9b5d.png)](https://gyazo.com/edf6f6bae7616c651ada838e0d4f9b5d)

右上のLogin画面へのリンクをクリックし、ログイン画面へ遷移します。
[![Image from Gyazo](https://i.gyazo.com/7a99dff09f7c4bf5ae1aa36300282b40.png)](https://gyazo.com/7a99dff09f7c4bf5ae1aa36300282b40)

先ほど登録したユーザでログインします。
[![Image from Gyazo](https://i.gyazo.com/09dfd7869a6408fec72b9783050160f1.png)](https://gyazo.com/09dfd7869a6408fec72b9783050160f1)


すると右上にショッピングカートのマークが出ているかと思います。またカートに入っている商品数も表示されております。ではアイコンをクリックしてショッピングカート画面へ遷移してみましょう。
[![Image from Gyazo](https://i.gyazo.com/88b6f18c1b94a0a0b38e3a7241954fbe.png)](https://gyazo.com/88b6f18c1b94a0a0b38e3a7241954fbe)

ショッピングカート画面へ遷移し、カートが空ですのメッセージが出てきます。
[![Image from Gyazo](https://i.gyazo.com/139c0bc941a32bfbef19454603ec7066.png)](https://gyazo.com/139c0bc941a32bfbef19454603ec7066)

それでは次にサーチバーに"アイロン"と入力し、商品を検索します。
[![Image from Gyazo](https://i.gyazo.com/f934865c36a54970c1001a9057c67c29.png)](https://gyazo.com/f934865c36a54970c1001a9057c67c29)

検索された商品のリンクをクリックし、詳細画面へ遷移します。
[![Image from Gyazo](https://i.gyazo.com/43c4553dc260c0d74eeb107a85920928.png)](https://gyazo.com/43c4553dc260c0d74eeb107a85920928)

ショッピングカートに追加するボタンが表示されているのでクリックします。
[![Image from Gyazo](https://i.gyazo.com/97fee05ec5b0db7ee298abac6e818574.png)](https://gyazo.com/97fee05ec5b0db7ee298abac6e818574)

ショッピングカート画面へ遷移し、追加した商品が表示されていることを確認します。

その他商品を追加したり削除したりしてみましょう。
また、後ほど利用するので、ショッピングカート画面のURLをコピーしておきます。
(`http://localhost:8000/techpit/amazon/cart/1`のようになっているはずです)

次にログアウトした状態でショッピングカート画面へのリンクが表示されないこと、またその画面へのアクセスができないことを確認しましょう。

ではまず右上のリンクからログアウトしてください。
[![Image from Gyazo](https://i.gyazo.com/e05ecb3934801551ff03375f0d282a1d.png)](https://gyazo.com/e05ecb3934801551ff03375f0d282a1d)

するとショッピングカート画面へのリンクが表示されていないことが確認できます。

ではURLで指定してショッピングカート画面へログインしてみましょう。するとログイン画面へリダイレクトされると思います。これでログインしていないとショッピングカート画面へアクセスできないことが確認できました。
[![Image from Gyazo](https://i.gyazo.com/52a01131d047693bab36e70899077bb6.png)](https://gyazo.com/52a01131d047693bab36e70899077bb6)


以上で今回のパートは終了です。

お疲れ様でした。
