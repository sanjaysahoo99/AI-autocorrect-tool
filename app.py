from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    corrected_text = ""

    if request.method == "POST":

        user_text = request.form["text"]

        blob = TextBlob(user_text)

        corrected_text = str(blob.correct())

    return render_template(
        "index.html",
        corrected=corrected_text
    )

if __name__ == "__main__":
    app.run(debug=True)