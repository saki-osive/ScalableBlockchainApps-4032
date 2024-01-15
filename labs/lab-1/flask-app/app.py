from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
            "https://media.glamour.com/photos/580e1dc07a52574c7ef91071/master/w_1920%2Cc_limit/giphy%2520(1).gif",
            "https://media.glamour.com/photos/580e1edafa71013257a9180f/master/w_1920%2Cc_limit/giphy%2520(2).gif",
            "https://media.glamour.com/photos/580e1f287cbc533f7e7eae0d/master/w_1920%2Cc_limit/giphy%2520(5).gif",
            "https://media.glamour.com/photos/580e1f078bd9950546d001f5/master/w_1920%2Cc_limit/giphy%2520(6).gif",
            "https://media.glamour.com/photos/580e1f31114e233c0c9c84fc/master/w_1920%2Cc_limit/giphy%2520(7).gif"
        ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")