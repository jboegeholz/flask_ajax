from flask import Flask, jsonify
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def item_list():
    return render_template("item_list.html")


@app.route('/_items')
def items():
    filter = request.args.get('filter', "", type=str)
    items = ["apple", "banana", "lemon"]

    filtered_items = []
    for item in items:
        if filter in item:
            filtered_items.append(item)
    return jsonify(items=filtered_items)

if __name__ == '__main__':
    app.run()
