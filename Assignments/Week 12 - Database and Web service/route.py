

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/statkode')
def index():
    data = pd.read_csv("befkbhalderstatkode.csv")
    return data.to_html()


if __name__ == '__main__':
    app.run(debug=True)
