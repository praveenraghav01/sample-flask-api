from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
image_urls_map = {
    "https://assets.getsimpl.com/images/merchants-page-list/bb.png": "https://www.bigbasket.com/",
    "https://assets.getsimpl.com/images/merchants-page-list/zomato.png": "https://www.zomato.com/",
    "https://assets.getsimpl.com/images/merchants-page-list/dunzo.png": "https://www.dunzo.com/bangalore",
    "https://assets.getsimpl.com/images/merchants-page-list/jiomart.png": "https://www.jiomart.com/",
}


@app.route("/")
def index():
    key = random.choice(list(image_urls_map))
    return render_template("index.html", simpl_url=image_urls_map, image_url=key)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
