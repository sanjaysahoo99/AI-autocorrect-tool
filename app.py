from flask import Flask, render_template, request
from textblob import TextBlob
import language_tool_python

app = Flask(__name__)

tool = language_tool_python.LanguageTool('en-US')

@app.route("/", methods=["GET", "POST"])
def home():

    corrected_text = ""

    if request.method == "POST":

        user_text = request.form["text"]

     
        blob = TextBlob(user_text)
        spelling_corrected = str(blob.correct())

        
        matches = tool.check(spelling_corrected)
        corrected_text = language_tool_python.utils.correct(
            spelling_corrected,
            matches
        )

    return render_template(
        "index.html",
        corrected=corrected_text
    )

if __name__ == "__main__":
    app.run(debug=True)