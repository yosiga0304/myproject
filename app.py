from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 初期状態
money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}

@app.route('/')
def index():
    global money
    return render_template('index.html', items=items, money=money)

@app.route('/buy/<item_name>', methods=['POST'])
def buy(item_name):
    global money
    item_price = items[item_name]
    input_count = int(request.form['count'])
    total_price = item_price * input_count

    if money >= total_price:
        money -= total_price
        message = f"{item_name}を{input_count}個買いました。"
        if money == 0:
            message += "財布が空になりました"
    else:
        message = f"お金が足りません。{item_name}を買えませんでした。"

    return render_template('index.html', items=items, money=money, message=message)

if __name__ == '__main__':
    app.run(debug=True)



