from time import sleep

from flask import Flask, jsonify
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    hello_string = "Hello World"
    return render_template("index.html",
                           hello_message=hello_string)


@app.route('/static_item_list')
def static_item_list():
    fruits = ["Apple", "Banana", "Lemon"]
    return render_template("static_item_list.html", fruits=fruits)


@app.route('/item_list_with_filter', methods=["GET", "POST"])
def item_list_with_filter():
    fruits = ["Apple", "Banana", "Lemon"]

    if "filter" in request.form:
        fruit_filter_value = request.form["filter"]
    else:
        fruit_filter_value = ""

    filtered_items = []
    for fruit in fruits:
        if fruit_filter_value.lower() in fruit.lower():
            filtered_items.append(fruit)

    return render_template("item_list_with_filter.html",
                           fruits=filtered_items)


@app.route('/dynamic_item_list')
def dynamic_item_list():
    return render_template("dynamic_item_list.html")


@app.route('/_items')
def items():
    fruit_filter_value = request.args.get('filter', "", type=str)
    fruits = ["Apple", "Banana", "Lemon"]

    filtered_items = []
    for fruit in fruits:
        if fruit_filter_value.lower() in fruit.lower():
            filtered_items.append(fruit)

    sleep(1)  # to simulate latency on the server side
    return jsonify(fruits=filtered_items)

if __name__ == '__main__':
    app.run()
